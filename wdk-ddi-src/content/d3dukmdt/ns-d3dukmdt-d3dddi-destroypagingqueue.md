---
UID: NS.d3dukmdt.D3DDDI_DESTROYPAGINGQUEUE
title: D3DDDI_DESTROYPAGINGQUEUE
author: windows-driver-content
description: D3DDDI_DESTROYPAGINGQUEUE is used with pfnDestroyPagingQueueCb and D3DKMTDestroyPagingQueue to wait for a paging queue to finish all operations queued to it and destroy it along with the associated sync object.
old-location: display\d3dddi_destroypagingqueue.htm
old-project: display
ms.assetid: CBCE6C4C-C713-4ED3-9C40-30F9D8C2406D
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_DESTROYPAGINGQUEUE, D3DDDI_DESTROYPAGINGQUEUE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_DESTROYPAGINGQUEUE
req.alt-loc: d3dukmdt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# D3DDDI_DESTROYPAGINGQUEUE structure



## -description
<p><b>D3DDDI_DESTROYPAGINGQUEUE</b> is used with <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroypagingqueuecb.md">pfnDestroyPagingQueueCb</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/dn906773">D3DKMTDestroyPagingQueue</a> to wait for a paging queue to finish all operations queued to it and destroy it along with the associated sync object.</p>


## -syntax

````
typedef struct D3DDDI_DESTROYPAGINGQUEUE {
  D3DKMT_HANDLE hPagingQueue;
} D3DDDI_DESTROYPAGINGQUEUE;
````


## -struct-fields
<dl>

### -field <b>hPagingQueue</b>

<dd>
<p>[in] A paging queue handle to be destroyed.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroypagingqueuecb.md">pfnDestroyPagingQueueCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906773">D3DKMTDestroyPagingQueue</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_DESTROYPAGINGQUEUE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
