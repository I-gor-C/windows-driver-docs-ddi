---
UID: NS.d3dumddi._D3DDDI_ADAPTERCALLBACKS
title: D3DDDI_ADAPTERCALLBACKS
author: windows-driver-content
description: The D3DDDI_ADAPTERCALLBACKS structure contains Microsoft Direct3D runtime callback functions that the user-mode display driver can use.
old-location: display\d3dddi_adaptercallbacks.htm
old-project: display
ms.assetid: b912449b-45d1-473d-aa14-b3f3ffbfefff
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_ADAPTERCALLBACKS, D3DDDI_ADAPTERCALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_ADAPTERCALLBACKS
req.alt-loc: d3dumddi.h
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

# D3DDDI_ADAPTERCALLBACKS structure



## -description
<p>The D3DDDI_ADAPTERCALLBACKS structure contains Microsoft Direct3D runtime callback functions that the user-mode display driver can use.</p>


## -syntax

````
typedef struct _D3DDDI_ADAPTERCALLBACKS {
  PFND3DDDI_QUERYADAPTERINFOCB         pfnQueryAdapterInfoCb;
  PFND3DDDI_GETMULTISAMPLEMETHODLISTCB pfnGetMultisampleMethodListCb;
} D3DDDI_ADAPTERCALLBACKS;
````


## -struct-fields
<dl>

### -field <b>pfnQueryAdapterInfoCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-queryadapterinfocb.md">pfnQueryAdapterInfoCb</a> function, which the user-mode display driver uses to query the display miniport driver for adapter configuration information.</p>
</dd>

### -field <b>pfnGetMultisampleMethodListCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getmultisamplemethodlistcb.md">pfnGetMultisampleMethodListCb</a> function, which the user-mode display driver uses to retrieve the list of multiple-sampling methods that are used for an allocation.</p>
</dd>
</dl>

## -remarks
<p>The following code example demonstrates the function declarations for the functions that the members of D3DDDI_ADAPTERCALLBACKS point to.</p>

## -requirements
<table>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543226">D3DDDIARG_OPENADAPTER</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-openadapter.md">OpenAdapter</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getmultisamplemethodlistcb.md">pfnGetMultisampleMethodListCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-queryadapterinfocb.md">pfnQueryAdapterInfoCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_ADAPTERCALLBACKS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
