from functools import partial
import subprocess


def internal(transform, ctx, arg):
    args = arg.split(":", 1)
    num_words = int(args[0])
    expr = args[1]

    raw_words = ctx.last_words(count=num_words)
    words = [w.strip() for w in words]
    text = "".join(raw_words)

    action = ctx.copy_last_action()
    action.prev_replace = text
    action.word = None
    action.prev_attach = True
    action.text = str(transform(expr, raw_words, words, text))

    return action


def run_cmd(expr, raw_words, words, text):
    env = {"TEXT": text}

    p = subprocess.Popen(
        expr,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        env=env,
    )

    out, err = p.communicate()

    return out.decode().strip()


retro_stringop = partial(internal, lambda expr, raw_words, words, text: eval(expr))
retro_stringop_sh = partial(internal, run_cmd)
