---
UID : NC:dispmprt.DXGKCB_READ_DEVICE_SPACE
title : DXGKCB_READ_DEVICE_SPACE
author : windows-driver-content
description : The DxgkCbReadDeviceSpace function reads from a device configuration space or the expansion ROM of a display adapter.
old-location : display\dxgkcbreaddevicespace.htm
old-project : display
ms.assetid : 118ea0b9-6463-4050-9f33-192a3d42fdce
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _SYMBOL_INFO_EX, *PSYMBOL_INFO_EX, SYMBOL_INFO_EX
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : dispmprt.h
req.include-header : Dispmprt.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DxgkCbReadDeviceSpace
req.alt-loc : dispmprt.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PSYMBOL_INFO_EX, SYMBOL_INFO_EX"
---


# DXGKCB_READ_DEVICE_SPACE callback function
The <b>DxgkCbReadDeviceSpace</b> function reads from a device configuration space or the expansion ROM of a display adapter.

## Syntax

```
DXGKCB_READ_DEVICE_SPACE DxgkcbReadDeviceSpace;

NTSTATUS DxgkcbReadDeviceSpace(
  HANDLE DeviceHandle,
  ULONG DataType,
  PVOID Buffer,
  ULONG Offset,
  ULONG Length,
  PULONG BytesRead
)
{...}
```

## Parameters

`DeviceHandle`

A handle that represents a display adapter. The display miniport driver previously obtained this handle in the <b>DeviceHandle</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560942">DXGKRNL_INTERFACE</a> structure that was passed to <a href="..\dispmprt\nc-dispmprt-dxgkddi_start_device.md">DxgkDdiStartDevice</a>.

`DataType`

The type of read transaction to be performed. This parameter must be one of the following values, which are defined in <i>Dispmprt.h</i>.

`Buffer`

A pointer to a caller-allocated buffer that receives the data read from the configuration space or ROM.

`Offset`

The offset, into the configuration space or the expansion ROM, at which the read transaction begins.

`Length`

The number of bytes to be read.

`BytesRead`

A pointer to a ULONG-typed variable that receives the number of bytes actually read.


## Return Value

<b>DxgkCbReadDeviceSpace</b> returns one of the following values:
<dl>
<dt><b>  STATUS_SUCCESS</b></dt>
</dl>  The function succeeded.
<dl>
<dt><b>  STATUS_INVALID_PARAMETER</b></dt>
</dl>  The <i>DeviceHandle</i>, <i>DataType</i>, or <i>Buffer</i> parameter is invalid.
<dl>
<dt><b>  STATUS_UNSUCCESSFUL</b></dt>
</dl>  The function was unable to read the data.

 

The following code example reads a value of a specific size from the PCI configuration space.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dispmprt.h (include Dispmprt.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkcb_write_device_space.md">DxgkCbWriteDeviceSpace</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_READ_DEVICE_SPACE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>