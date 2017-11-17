# Declarations in the wdfcommonbuffer header
This header Wdfcommonbuffer contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_COMMON_BUFFER_CONFIG structure](ns-wdfcommonbuffer--wdf-common-buffer-config.md) | The WDF_COMMON_BUFFER_CONFIG structure contains configuration information for a common buffer. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfCommonBufferGetAlignedVirtualAddress function](nf-wdfcommonbuffer-wdfcommonbuffergetalignedvirtualaddress.md) | The WdfCommonBufferGetAlignedVirtualAddress method returns the virtual address that is associated with a specified common buffer. |
| [WdfCommonBufferCreate function](nf-wdfcommonbuffer-wdfcommonbuffercreate.md) | The WdfCommonBufferCreate method creates a memory buffer that both the driver and a direct memory access (DMA) device can access simultaneously. |
| [WdfCommonBufferCreateWithConfig function](nf-wdfcommonbuffer-wdfcommonbuffercreatewithconfig.md) | The WdfCommonBufferCreateWithConfig method creates a memory buffer that both the driver and a direct memory access (DMA) device can access simultaneously, and the method also specifies buffer configuration information. |
| [WdfCommonBufferGetLength function](nf-wdfcommonbuffer-wdfcommonbuffergetlength.md) | The WdfCommonBufferGetLength method returns the length of a specified common buffer. |
| [WDF_COMMON_BUFFER_CONFIG_INIT function](nf-wdfcommonbuffer-wdf-common-buffer-config-init.md) | The WDF_COMMON_BUFFER_CONFIG_INIT function initializes a WDF_COMMON_BUFFER_CONFIG structure. |
| [WdfCommonBufferGetAlignedLogicalAddress function](nf-wdfcommonbuffer-wdfcommonbuffergetalignedlogicaladdress.md) | The WdfCommonBufferGetAlignedLogicalAddress method returns the logical address that is associated with a specified common buffer. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFCOMMONBUFFERCREATE callback function](nc-wdfcommonbuffer-pfn-wdfcommonbuffercreate.md) | TBD |
| [PFN_WDFCOMMONBUFFERGETALIGNEDLOGICALADDRESS callback function](nc-wdfcommonbuffer-pfn-wdfcommonbuffergetalignedlogicaladdress.md) | TBD |
| [PFN_WDFCOMMONBUFFERGETLENGTH callback function](nc-wdfcommonbuffer-pfn-wdfcommonbuffergetlength.md) | TBD |
| [PFN_WDFCOMMONBUFFERCREATEWITHCONFIG callback function](nc-wdfcommonbuffer-pfn-wdfcommonbuffercreatewithconfig.md) | TBD |
| [PFN_WDFCOMMONBUFFERGETALIGNEDVIRTUALADDRESS callback function](nc-wdfcommonbuffer-pfn-wdfcommonbuffergetalignedvirtualaddress.md) | TBD |

This header is used in these topics:

- [wdf](..content/_wdf)
