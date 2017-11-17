---
UID: NS.d3dkmddi._DXGKARG_FORMATHISTORYBUFFER
title: DXGKARG_FORMATHISTORYBUFFER
author: windows-driver-content
description: Contains info for the display miniport driver to format a history buffer.
old-location: display\dxgkarg_formathistorybuffer.htm
ms.assetid: 40E00234-C22B-4F86-AC5D-197223298FD7
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,WDDM 1.3 and later
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_FORMATHISTORYBUFFER
req.alt-loc: D3dkmddi.h
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
ms.keywords: DXGKARG_FORMATHISTORYBUFFER, DXGKARG_FORMATHISTORYBUFFER
req.iface: 
---

# DXGKARG_FORMATHISTORYBUFFER structure



## -description
<p>Contains info for the display miniport driver to format a history buffer.</p>


## -syntax

````
typedef struct _DXGKARG_FORMATHISTORYBUFFER {
  DXGK_HISTORY_BUFFER            *pHistoryBuffer;
  UINT32                         HistoryBufferSize;
  PVOID                          pFormattedBuffer;
  UINT32                         FormattedBufferSize;
  UINT32                         NumTimestamps;
  DXGKARG_HISTORYBUFFERPRECISION Precision;
  UINT32                         Offset;
} DXGKARG_FORMATHISTORYBUFFER;
````


## -struct-fields
<dl>

### -field <b>pHistoryBuffer</b>

<dd>
<p>A pointer to the unformatted <a href="https://msdn.microsoft.com/library/windows/hardware/dn439361">DXGK_HISTORY_BUFFER</a> history buffer that was populated by the GPU.</p>
</dd>

### -field <b>HistoryBufferSize</b>

<dd>
<p>The size, in bytes, of the buffer pointed to by <b>pHistoryBuffer</b>.</p>
</dd>

### -field <b>pFormattedBuffer</b>

<dd>
<p>A pointer to a segment of non-paged system memory that the driver uses to store time stamp info that it derives from the provided unformatted history buffer.</p>
<p>The buffer pointed to by <b>pFormattedBuffer</b> should be managed as a large array of time stamps of precision specified by <b>Precision</b>. The buffer should not contain any header info that already exists in the original history buffer.</p>
</dd>

### -field <b>FormattedBufferSize</b>

<dd>
<p>The size, in bytes, of the buffer pointed to by <b>pFormattedBuffer</b>. The driver should ensure that it doesn't write data beyond this buffer size.</p>
</dd>

### -field <b>NumTimestamps</b>

<dd>
<p>The number of time stamps. On completion of a call to the <a href="https://msdn.microsoft.com/84417629-5C12-4CB5-B147-0A558A4F9090">DxgkDdiFormatHistoryBuffer</a> function, the driver should set this value to the number of time stamps that are written to the formatted buffer pointed to by <b>pFormattedBuffer</b>.</p>
<p>Note that the number of time stamps that will be in the formatted output buffer won't be known until the driver completes the formatted buffer pointed to by <b>pFormattedBuffer</b>.</p>
</dd>

### -field <b>Precision</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn439359">DXGKARG_HISTORYBUFFERPRECISION</a> structure that the driver fills with info on the precision of the time stamps that will be logged to the Event Tracing for Windows (ETW) facility.</p>
<p>The value of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn439359">DXGKARG_HISTORYBUFFERPRECISION</a>.<b>PrecisionBits</b> member cannot be zero.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>On input to a call to the <a href="https://msdn.microsoft.com/84417629-5C12-4CB5-B147-0A558A4F9090">DxgkDdiFormatHistoryBuffer</a> function, the value of this member is the offset to the first time stamp at which formatting should start. On completion of the function call, the driver should set the value to zero if it successfully formatted all the time stamps in the history buffer.</p>
<p>If nonzero, the driver could not format all the time stamps in the history buffer without filling the formatted buffer. In this case, the value represents the offset that should be continued from in the next function call.</p>
</dd>
</dl>

## -remarks
<p>The driver should obtain time stamp entries and the number of usable time stamps from the header of the provided history buffer. Any additional data that the driver needs for calculations should be stored in private data.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>WDDM 1.3 and later</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn439361">DXGK_HISTORY_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn439359">DXGKARG_HISTORYBUFFERPRECISION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/84417629-5C12-4CB5-B147-0A558A4F9090">DxgkDdiFormatHistoryBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_FORMATHISTORYBUFFER structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
