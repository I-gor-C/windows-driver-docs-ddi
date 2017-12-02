---
UID: NS.d3dkmthk._D3DKMT_TRIMNOTIFICATION
title: D3DKMT_TRIMNOTIFICATION
author: windows-driver-content
description: D3DKMT_TRIMNOTIFICATION is used to notify a driver to trim its memory residency list.
old-location: display\d3dkmt_trimnotification.htm
old-project: display
ms.assetid: 50E3F5CC-AFB9-4527-A812-44295373D80B
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_TRIMNOTIFICATION, D3DKMT_TRIMNOTIFICATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_TRIMNOTIFICATION
req.alt-loc: D3dkmthk.h
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

# D3DKMT_TRIMNOTIFICATION structure



## -description
<p><b>D3DKMT_TRIMNOTIFICATION</b> is used to notify a driver to trim its memory residency list.</p>


## -syntax

````
typedef struct _D3DKMT_TRIMNOTIFICATION {
  VOID                          *Context;
  D3DDDI_TRIMRESIDENCYSET_FLAGS Flags;
  UINT64                        NumBytesToTrim;
} D3DKMT_TRIMNOTIFICATION;
````


## -struct-fields
<dl>

### -field Context

<dd>
<p>[in] The caller-supplied context for the callback notification.</p>
</dd>

### -field Flags

<dd>
<p>[in] A <a href="..\d3dukmdt\ns-d3dukmdt-d3dddi-trimresidencyset-flags.md">D3DDDI_TRIMRESIDENCYSET_FLAGS</a> structure containing the trimming behavior flags.</p>
</dd>

### -field NumBytesToTrim

<dd>
<p>[in] When <b>TrimToBudget</b> is set, this value specifies how much the application should evict in order to meet its current memory budget.</p>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt-d3dddi-trimresidencyset-flags.md">D3DDDI_TRIMRESIDENCYSET_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_TRIMNOTIFICATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
