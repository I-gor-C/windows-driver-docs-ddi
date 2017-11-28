---
UID: NS.d3dkmddi._DXGK_HISTORY_BUFFER
title: DXGK_HISTORY_BUFFER
author: windows-driver-content
description: Specifies a history buffer that stores time stamps that record GPU activity throughout the execution lifetime of a direct memory access (DMA) buffer.
old-location: display\dxgk_history_buffer.htm
old-project: display
ms.assetid: 66088355-A110-4295-81D9-542491E2D6E4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_HISTORY_BUFFER, DXGK_HISTORY_BUFFER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,WDDM 1.3 and later
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_HISTORY_BUFFER
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
req.iface: 
---

# DXGK_HISTORY_BUFFER structure



## -description
<p>Specifies a history buffer that stores time stamps that record GPU activity throughout the execution lifetime of a direct memory access (DMA) buffer.</p>


## -syntax

````
typedef struct _DXGK_HISTORY_BUFFER {
  DXGK_HISTORY_BUFFER_HEADER Header;
  UINT8                      DriverPrivateData[1];
} DXGK_HISTORY_BUFFER;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>A pointer to  a <a href="https://msdn.microsoft.com/library/windows/hardware/dn439362">DXGK_HISTORY_BUFFER_HEADER</a> structure that contains history buffer header info.</p>
</dd>

### -field <b>DriverPrivateData</b>

<dd>
<p>An array that marks the beginning of the optional driver data and timestamp entries. See Remarks for more info.</p>
</dd>
</dl>

## -remarks
<p>You can calculate the address of the first time stamp in the history buffer by adding the value of <a href="https://msdn.microsoft.com/library/windows/hardware/dn439362">DXGK_HISTORY_BUFFER_HEADER</a>.<b>PrivateDataSize</b> to the address of <b>DriverPrivateData</b>.</p>

<p>The beginnings of the time stamps should be aligned to a 64-bit boundary.</p>

<p>The first and last time stamps in the <b>DriverPrivateData</b> array must be respectively the start and end times of the DMA buffer. Time stamps that are used to log marker times begin after this end time. This is the case for both formatted and unformatted buffers.</p>

<p>The driver specifies the precision of time stamps with the <a href="https://msdn.microsoft.com/library/windows/hardware/dn439359">DXGKARG_HISTORYBUFFERPRECISION</a> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn439362">DXGK_HISTORY_BUFFER_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn439359">DXGKARG_HISTORYBUFFERPRECISION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_HISTORY_BUFFER structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
