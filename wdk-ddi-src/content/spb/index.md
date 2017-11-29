# Spb.h header


This header is used by SPB. For more information, see
- [SPB](../_SPB/index.md)

Spb.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [SPB_TRANSFER_LIST_ENTRY_INIT_BUFFER_LIST function](nf-spb-spb-transfer-list-entry-init-buffer-list.md) | The SPB_TRANSFER_LIST_ENTRY_INIT_BUFFER_LIST function returns an SPB_TRANSFER_LIST_ENTRY structure that is initialized to describe a scatter-gather list.SPB_TRANSFER_LIST_ENTRY_INIT_BUFFER_LIST function returns an SPB_TRANSFER_LIST_ENTRY structure that is initialized to describe a scatter-gather list. |
| [SPB_TRANSFER_LIST_ENTRY_INIT_MDL function](nf-spb-spb-transfer-list-entry-init-mdl.md) | The SPB_TRANSFER_LIST_ENTRY_INIT_MDL function returns an SPB_TRANSFER_LIST_ENTRY structure that is initialized to use an MDL to describe a data buffer. |
| [SPB_TRANSFER_LIST_ENTRY_INIT_NON_PAGED function](nf-spb-spb-transfer-list-entry-init-non-paged.md) | The SPB_TRANSFER_LIST_ENTRY_INIT_NON_PAGED function returns an SPB_TRANSFER_LIST_ENTRY structure that is initialized to describe a simple data buffer in nonpaged memory. |
| [SPB_TRANSFER_LIST_ENTRY_INIT_SIMPLE function](nf-spb-spb-transfer-list-entry-init-simple.md) | The SPB_TRANSFER_LIST_ENTRY_INIT_SIMPLE function returns an SPB_TRANSFER_LIST_ENTRY structure that is initialized to describe a simple data buffer.SPB_TRANSFER_LIST_ENTRY_INIT_SIMPLE function returns an SPB_TRANSFER_LIST_ENTRY structure that is initialized to describe a simple data buffer. |
| [SPB_TRANSFER_LIST_INIT function](nf-spb-spb-transfer-list-init.md) | The SPB_TRANSFER_LIST_INIT function initializes an SPB_TRANSFER_LIST structure. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [SPB_TRANSFER_BUFFER structure](ns-spb-spb-transfer-buffer.md) | The SPB_TRANSFER_BUFFER structure describes the data buffer for an individual transfer in an I/O transfer sequence. |
| [SPB_TRANSFER_BUFFER_LIST_ENTRY structure](ns-spb-spb-transfer-buffer-list-entry.md) | The SPB_TRANSFER_BUFFER_LIST_ENTRY structure describes either a simple transfer buffer, or an element in an array of one or more transfer buffers. |
| [SPB_TRANSFER_LIST structure](ns-spb-spb-transfer-list.md) | The SPB_TRANSFER_LIST structure describes an I/O transfer sequence. |
| [SPB_TRANSFER_LIST_ENTRY structure](ns-spb-spb-transfer-list-entry.md) | The SPB_TRANSFER_LIST_ENTRY structure describes a single transfer in an I/O transfer sequence. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [SPB_TRANSFER_BUFFER_FORMAT enumeration](ne-spb-spb-transfer-buffer-format.md) | The SPB_TRANSFER_BUFFER_FORMAT enumeration specifies the format of the buffer that is described by an SPB_TRANSFER_BUFFER structure. |
| [SPB_TRANSFER_DIRECTION enumeration](ne-spb-spb-transfer-direction.md) | The SPB_TRANSFER_DIRECTION enumeration describes the direction (read or write) of a single transfer in an I/O transfer sequence. |
