import torch
import utility
import data
import model
import loss
from option import args
from trainer import Trainer


if __name__ == '__main__':
    torch.manual_seed(args.seed)
    checkpoint = utility.checkpoint(args)

    if checkpoint.ok:
        loader = data.Data(args)
        net = model.Model(args, checkpoint)
        loss = loss.Loss(args, checkpoint) if not args.test_only else None
        t = Trainer(args, loader, net, loss, checkpoint)
        while not t.terminate():
            t.test()

            checkpoint.done()


