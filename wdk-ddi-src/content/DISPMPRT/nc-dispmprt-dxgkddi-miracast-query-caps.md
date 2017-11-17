---
UID: NC.dispmprt.DXGKDDI_MIRACAST_QUERY_CAPS
title: DXGKDDI_MIRACAST_QUERY_CAPS
author: windows-driver-content
description: Queries the Miracast capabilities of the current display adapter.
old-location: display\dxgkddimiracastquerycaps.htm
ms.assetid: C10CAA33-C407-4183-9090-B9D78B07CD12
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkDdiMiracastQueryCaps
req.alt-loc: Dispmprt.h
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

# DXGKDDI_MIRACAST_QUERY_CAPS callback



## -description
<p>Queries the Miracast capabilities of the current display adapter. The operating system  calls this function only when the display adapter is first started and then stores the capabilities that are returned.<div class="alert"><b>Note</b>  The capabilities of the display adapter must not change while it is connected.</div>
<div> </div>
</p>


## -prototype

````
DXGKDDI_MIRACAST_QUERY_CAPS DxgkDdiMiracastQueryCaps;

NTSTATUS* DxgkDdiMiracastQueryCaps(
  _In_  PVOID              DriverContext,
  _In_  ULONG              MiracastCapsSize,
  _Out_ DXGK_MIRACAST_CAPS *MiracastCaps
)
{ ... }
````


## -parameters
<dl>

### -param <i>DriverContext</i> [in]

<dd>
<p>A handle to a context block that is associated with a display adapter. The display miniport driver's <a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a> function previously provided this handle to the DirectX graphics kernel subsystem.</p>
</dd>

### -param <i>MiracastCapsSize</i> [in]

<dd>
<p>The size, supplied by the operating system, of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn322054">DXGK_MIRACAST_CAPS</a> structure pointed to by the <i>MiracastCaps</i> parameter.</p>
<p>The driver should check this value before it fills the structure.</p>
</dd>

### -param <i>MiracastCaps</i> [out]

<dd>
<p>A pointer to an operating system-provided buffer that holds a <a href="https://msdn.microsoft.com/library/windows/hardware/dn322054">DXGK_MIRACAST_CAPS</a> structure that the driver fills with Miracast device capabilities.</p>
</dd>
</dl>

## -returns
<p>Returns <b>STATUS_SUCCESS</b> if it succeeds. Otherwise, it returns one of the error codes that are defined in Ntstatus.h.</p>

## -remarks
<p>The operating system guarantees that this function follows the third-level synchronization mode as defined in <a href="https://msdn.microsoft.com/780d37d9-40c6-4737-9042-473810868227">Threading and Synchronization Third Level</a>.</p>

<p>The operating system guarantees that this function follows the third-level synchronization mode as defined in <a href="https://msdn.microsoft.com/780d37d9-40c6-4737-9042-473810868227">Threading and Synchronization Third Level</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn322054">DXGK_MIRACAST_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_MIRACAST_QUERY_CAPS callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
