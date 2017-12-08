# Lowio.h header


This header is used by Installable file system. For more information, see
- [Installable file system](../_ifsk/index.md)

Lowio.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [RxLowIoCompletion function](nf-lowio-rxlowiocompletion.md) | RxLowIoCompletion must be called by the network mini-redirector low I/O routines when they complete, if the low I/O routines have initially returned STATUS_PENDING. |
| [RxLowIoGetBufferAddress function](nf-lowio-rxlowiogetbufferaddress.md) | RxLowIoGetBufferAddress returns the buffer corresponding to the MDL from LowIoContext structure of an RX_CONTEXT structure. |
