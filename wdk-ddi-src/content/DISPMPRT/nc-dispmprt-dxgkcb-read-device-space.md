---
UID: NC.dispmprt.DXGKCB_READ_DEVICE_SPACE
title: DXGKCB_READ_DEVICE_SPACE
author: windows-driver-content
description: The DxgkCbReadDeviceSpace function reads from a device configuration space or the expansion ROM of a display adapter.
old-location: display\dxgkcbreaddevicespace.htm
ms.assetid: 118ea0b9-6463-4050-9f33-192a3d42fdce
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkCbReadDeviceSpace
req.alt-loc: dispmprt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
req.iface: IDebugSystemObjects4
---

# DXGKCB_READ_DEVICE_SPACE callback



## -description
<p>The <b>DxgkCbReadDeviceSpace</b> function reads from a device configuration space or the expansion ROM of a display adapter.</p>


## -prototype

````
DXGKCB_READ_DEVICE_SPACE DxgkCbReadDeviceSpace;

NTSTATUS DxgkCbReadDeviceSpace(
  _In_  HANDLE DeviceHandle,
  _In_  ULONG  DataType,
  _In_  PVOID  Buffer,
  _In_  ULONG  Offset,
  _In_  ULONG  Length,
  _Out_ PULONG BytesRead
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceHandle</i> [in]

<dd>
<p>A handle that represents a display adapter. The display miniport driver previously obtained this handle in the <b>DeviceHandle</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560942">DXGKRNL_INTERFACE</a> structure that was passed to <a href="https://msdn.microsoft.com/ffacbb39-2581-4207-841d-28ce57fbc64d">DxgkDdiStartDevice</a>.</p>
</dd>

### -param <i>DataType</i> [in]

<dd>
<p>The type of read transaction to be performed. This parameter must be one of the following values, which are defined in <i>Dispmprt.h</i>.</p>
<p></p>
<dl>

### -param <a id="DXGK_WHICHSPACE_BRIDGE"></a><a id="dxgk_whichspace_bridge"></a>DXGK_WHICHSPACE_BRIDGE

<dd>
<p>Read from the PCI Express (PCIe) root port's configuration space.</p>
</dd>

### -param <a id="DXGK_WHICHSPACE_CONFIG"></a><a id="dxgk_whichspace_config"></a>DXGK_WHICHSPACE_CONFIG

<dd>
<p>Read from the display adapter's configuration space.</p>
</dd>

### -param <a id="DXGK_WHICHSPACE_MCH"></a><a id="dxgk_whichspace_mch"></a>DXGK_WHICHSPACE_MCH

<dd>
<p>Read from the configuration space of a memory controller hub that is a peer to the adapter's parent bus.</p>
</dd>

### -param <a id="DXGK_WHICHSPACE_ROM"></a><a id="dxgk_whichspace_rom"></a>DXGK_WHICHSPACE_ROM

<dd>
<p>Read from the display adapter's expansion ROM.</p>
</dd>
</dl>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to a caller-allocated buffer that receives the data read from the configuration space or ROM.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>The offset, into the configuration space or the expansion ROM, at which the read transaction begins.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes to be read.</p>
</dd>

### -param <i>BytesRead</i> [out]

<dd>
<p>A pointer to a ULONG-typed variable that receives the number of bytes actually read.</p>
</dd>
</dl>

## -returns
<p><b>DxgkCbReadDeviceSpace</b> returns one of the following values:</p><dl>
<dt><b>  STATUS_SUCCESS</b></dt>
</dl><p>  The function succeeded.</p><dl>
<dt><b>  STATUS_INVALID_PARAMETER</b></dt>
</dl><p>  The <i>DeviceHandle</i>, <i>DataType</i>, or <i>Buffer</i> parameter is invalid.</p><dl>
<dt><b>  STATUS_UNSUCCESSFUL</b></dt>
</dl><p>  The function was unable to read the data.</p>

<p> </p>

<p>The following code example reads a value of a specific size from the PCI configuration space.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/797d6b0c-91a4-4923-ad40-937cfde50067">DxgkCbWriteDeviceSpace</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_READ_DEVICE_SPACE callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
