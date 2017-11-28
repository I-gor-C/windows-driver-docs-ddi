---
UID: NC.dispmprt.DXGKCB_MIRACAST_REPORT_CHUNK_INFO
title: DXGKCB_MIRACAST_REPORT_CHUNK_INFO
author: windows-driver-content
description: Called by the display miniport driver to report info about an encode chunk.
old-location: display\dxgkcbreportchunkinfo.htm
old-project: display
ms.assetid: 94A99749-EF80-4593-B03C-54A7AA2BDFC8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkCbReportChunkInfo
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
req.irql: Can be called at any IRQL level.
req.iface: IDebugSystemObjects4
---

# DXGKCB_MIRACAST_REPORT_CHUNK_INFO callback



## -description
<p>Called by the display miniport driver to report info about an encode chunk.</p>


## -prototype

````
DXGKCB_MIRACAST_REPORT_CHUNK_INFO DxgkCbReportChunkInfo;

NTSTATUS* DxgkCbReportChunkInfo(
  _In_ HANDLE                   MiracastHandle,
  _In_ DXGK_MIRACAST_CHUNK_INFO *pChunkInfo,
  _In_ PVOID                    pPrivateDriverData,
  _In_ UINT                     PrivateDataDriverSize
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiracastHandle</i> [in]

<dd>
<p>A driver-supplied handle to the Miracast display device. This handle was originally passed in the <b>MiracastHandle</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn344648">DXGK_MIRACAST_DISPLAY_CALLBACKS</a> structure in a call to the <a href="..\dispmprt\nc-dispmprt-dxgkddi-miracast-create-context.md">DxgkDdiMiracastCreateContext</a> function.</p>
</dd>

### -param <i>pChunkInfo</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn322056">DXGK_MIRACAST_CHUNK_INFO</a> structure that contains chunk information that is to be reported by the display miniport driver.</p>
</dd>

### -param <i>pPrivateDriverData</i> [in]

<dd>
<p>Reserved for system use. Must be set to <b>NULL</b>.</p>
</dd>

### -param <i>PrivateDataDriverSize</i> [in]

<dd>
<p>Reserved for system use. Must be set to zero.</p>
</dd>
</dl>

## -returns
<p>Returns <b>STATUS_SUCCESS</b> if it successfully delivers the message. Otherwise, it returns one of the error codes that are defined in Ntstatus.h.</p>

## -remarks
<p>The display miniport driver  calls this function when it wants to report chunk info to the operating system but won't create a chunk packet that will be queued in kernel mode and retrieved by the user-mode <a href="..\netdispumdddi\nc-netdispumdddi-pfn-get-next-chunk-data.md">GetNextChunkData</a> function.  This call only logs Event Tracing for Windows (ETW) events and takes no other action.</p>

<p>The display miniport driver  calls this function when it wants to report chunk info to the operating system but won't create a chunk packet that will be queued in kernel mode and retrieved by the user-mode <a href="..\netdispumdddi\nc-netdispumdddi-pfn-get-next-chunk-data.md">GetNextChunkData</a> function.  This call only logs Event Tracing for Windows (ETW) events and takes no other action.</p>

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
<p>Can be called at any IRQL level.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn322056">DXGK_MIRACAST_CHUNK_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn344648">DXGK_MIRACAST_DISPLAY_CALLBACKS</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-miracast-create-context.md">DxgkDdiMiracastCreateContext</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-get-next-chunk-data.md">GetNextChunkData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_MIRACAST_REPORT_CHUNK_INFO callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
