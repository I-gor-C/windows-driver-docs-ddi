---
UID: NS.d3dumddi._D3DDDICB_CREATESYNCHRONIZATIONOBJECT2
title: D3DDDICB_CREATESYNCHRONIZATIONOBJECT2
author: windows-driver-content
description: Describes a synchronization object that the pfnCreateSynchronizationObject2Cb function creates.
old-location: display\d3dddicb_createsynchronizationobject2.htm
old-project: display
ms.assetid: 090fe0df-d2b4-4bfd-a3f3-38bc228337ab
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_CREATESYNCHRONIZATIONOBJECT2, D3DDDICB_CREATESYNCHRONIZATIONOBJECT2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_CREATESYNCHRONIZATIONOBJECT2
req.alt-loc: D3dumddi.h
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

# D3DDDICB_CREATESYNCHRONIZATIONOBJECT2 structure



## -description
<p>Describes a synchronization object that the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createsynchronizationobject2cb.md">pfnCreateSynchronizationObject2Cb</a> function creates.</p>


## -syntax

````
typedef struct _D3DDDICB_CREATESYNCHRONIZATIONOBJECT2 {
  D3DDDI_SYNCHRONIZATIONOBJECTINFO2 Info;
  D3DKMT_HANDLE                     hSyncObject;
} D3DDDICB_CREATESYNCHRONIZATIONOBJECT2;
````


## -struct-fields
<dl>

### -field <b>Info</b>

<dd>
<p>[in] A <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-synchronizationobjectinfo2.md">D3DDDI_SYNCHRONIZATIONOBJECTINFO2</a> structure that contains information about the kernel-mode synchronization object to create.</p>
</dd>

### -field <b>hSyncObject</b>

<dd>
<p>[out] A <b>D3DKMT_HANDLE</b> value that represents a kernel-mode handle to the created kernel-mode GPU synchronization object.</p>
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
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-synchronizationobjectinfo2.md">D3DDDI_SYNCHRONIZATIONOBJECTINFO2</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createsynchronizationobject2cb.md">pfnCreateSynchronizationObject2Cb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_CREATESYNCHRONIZATIONOBJECT2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
