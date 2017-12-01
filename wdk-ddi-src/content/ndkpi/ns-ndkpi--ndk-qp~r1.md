---
UID: NS.ndkpi._NDK_QP~r1
title: NDK_QP
author: windows-driver-content
description: The NDK_QP structure specifies the attributes of an NDK queue pair (QP) object.
old-location: netvista\ndk_qp.htm
old-project: netvista
ms.assetid: 43491796-35CA-4E0C-90EF-7148651C68A6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDK_QP, NDK_QP
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDK_QP
req.alt-loc: ndkpi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# NDK_QP structure



## -description
<p>The <b>NDK_QP</b> structure specifies the attributes of an NDK queue pair (QP) object.</p>


## -syntax

````
typedef struct _NDK_QP {
  NDK_OBJECT_HEADER     Header;
  CONST NDK_QP_DISPATCH *Dispatch;
} NDK_QP;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The <a href="..\ndkpi\ns-ndkpi--ndk-object-header.md">NDK_OBJECT_HEADER</a> structure for the <b>NDK_QP</b> structure. Set the <b>ObjectType</b> member of the structure that <b>Header</b> specifies to <b>NdkObjectTypeQp</b>.</p>
</dd>

### -field <b>Dispatch</b>

<dd>
<p>A pointer to an <a href="..\ndkpi\ns-ndkpi--ndk-qp-dispatch.md">NDK_QP_DISPATCH</a> structure that defines dispatch functions for the NDK QP object.</p>
</dd>
</dl>

## -remarks
<p>An NDK provider must set the <b>Dispatch</b> member to point to its  <a href="..\ndkpi\ns-ndkpi--ndk-qp-dispatch.md">NDK_QP_DISPATCH</a> table before returning the  created QP object. Also, the NDK provider must not use the <b>Dispatch</b> member after setting it because the NDK consumer can change the <b>Dispatch</b> member to some other value.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>None supported</p>
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
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndkpi.h (include Ndkpi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-object-header.md">NDK_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-qp-dispatch.md">NDK_QP_DISPATCH</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-close-object.md">NDK_FN_CLOSE_OBJECT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-completion.md">NDK_FN_CREATE_COMPLETION</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-qp.md">NDK_FN_CREATE_QP</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-qp-with-srq.md">NDK_FN_CREATE_QP_WITH_SRQ</a>
</dt>
<dt>
<a href="NULL">NDKPI Object Lifetime Requirements</a>
</dt>
<dt>
<a href="NULL">NDKPI Work Request Posting Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_QP structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
