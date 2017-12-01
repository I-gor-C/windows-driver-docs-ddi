---
UID: NS.ndkpi._NDK_CQ
title: NDK_CQ
author: windows-driver-content
description: The NDK_CQ structure specifies the attributes of an NDK completion queue (CQ) object.
old-location: netvista\ndk_cq.htm
old-project: netvista
ms.assetid: FE5E1E5F-3EEC-4FF4-B275-E2B086ADCDCC
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDK_CQ,
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
req.alt-api: NDK_CQ
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

# NDK_CQ structure



## -description
<p>The <b>NDK_CQ</b> structure specifies the attributes of an NDK completion queue (CQ) object.</p>


## -syntax

````
typedef struct _NDK_CQ {
  NDK_OBJECT_HEADER     Header;
  CONST NDK_CQ_DISPATCH *Dispatch;
} NDK_CQ, *PNDK_CQ;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The <a href="..\ndkpi\ns-ndkpi--ndk-object-header.md">NDK_OBJECT_HEADER</a> structure for the NDK_CQ structure. Set the <b>ObjectType</b> member of the structure that <b>Header</b> specifies to <b>NdkObjectTypeCq</b>.</p>
</dd>

### -field <b>Dispatch</b>

<dd>
<p>A pointer to an <a href="..\ndkpi\ns-ndkpi--ndk-cq-dispatch.md">NDK_CQ_DISPATCH</a> structure that defines dispatch functions for the NDK CQ object.</p>
</dd>
</dl>

## -remarks
<p>An NDK provider must set the <b>Dispatch</b> member to point to its  <a href="..\ndkpi\ns-ndkpi--ndk-cq-dispatch.md">NDK_CQ_DISPATCH</a> table before returning the  created CQ object. Also, the NDK provider must not use the <b>Dispatch</b> member after setting it because the NDK consumer can change the <b>Dispatch</b> member to some other value.</p>

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
<a href="..\ndkpi\ns-ndkpi--ndk-cq-dispatch.md">NDK_CQ_DISPATCH</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-object-header.md">NDK_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-close-object.md">NDK_FN_CLOSE_OBJECT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-completion.md">NDK_FN_CREATE_COMPLETION</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-cq.md">NDK_FN_CREATE_CQ</a>
</dt>
<dt>
<a href="NULL">NDKPI Completion Handling Requirements</a>
</dt>
<dt>
<a href="NULL">NDKPI Object Lifetime Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_CQ structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
