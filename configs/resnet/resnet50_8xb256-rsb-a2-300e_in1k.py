_base_ = [
    '../_base_/models/resnet50.py',
    '../_base_/datasets/imagenet_bs256_rsb_a12.py',
    '../_base_/schedules/imagenet_bs2048_rsb.py',
    '../_base_/default_runtime.py'
]

# model settings
model = dict(
    backbone=dict(
        norm_cfg=dict(type='SyncBN', requires_grad=True),
        drop_path_rate=0.05,
    ),
    head=dict(loss=dict(use_sigmoid=True)),
    train_cfg=dict(augments=[
        dict(type='Mixup', alpha=0.1, num_classes=1000),
        dict(type='CutMix', alpha=1.0, num_classes=1000)
    ]))

# dataset settings
train_dataloader = dict(sampler=dict(type='RepeatAugSampler', shuffle=True))

# schedule settings
optim_wrapper = dict(
    paramwise_cfg=dict(bias_decay_mult=0., norm_decay_mult=0.))

train_cfg = dict(by_epoch=True, max_epochs=300)
