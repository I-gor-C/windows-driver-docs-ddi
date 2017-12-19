---
UID: NS.NDKPI._NDK_CQ~R1
title: _NDK_CQ
author: windows-driver-content
description: The NDK_CQ structure specifies the attributes of an NDK completion queue (CQ) object.
old-location: netvista\ndk_cq.htm
old-project: NetVista
ms.assetid: FE5E1E5F-3EEC-4FF4-B275-E2B086ADCDCC
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _NDK_CQ, NDK_CQ
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
---

# _NDK_CQ structure



## -description
The <b>NDK_CQ</b> structure specifies the attributes of an NDK completion queue (CQ) object.



## -syntax

````
typedef struct _NDK_CQ {
  NDK_OBJECT_HEADER     Header;
  CONST NDK_CQ_DISPATCH *Dispatch;
} NDK_CQ, *PNDK_CQ;
````


## -struct-fields

### -field Header

The <a href="netvista.ndk_object_header">NDK_OBJECT_HEADER</a> structure for the NDK_CQ structure. Set the <b>ObjectType</b> member of the structure that <b>Header</b> specifies to <b>NdkObjectTypeCq</b>.


### -field Dispatch

A pointer to an <a href="netvista.ndk_cq_dispatch">NDK_CQ_DISPATCH</a> structure that defines dispatch functions for the NDK CQ object.


## -remarks
An NDK provider must set the <b>Dispatch</b> member to point to its  <a href="netvista.ndk_cq_dispatch">NDK_CQ_DISPATCH</a> table before returning the  created CQ object. Also, the NDK provider must not use the <b>Dispatch</b> member after setting it because the NDK consumer can change the <b>Dispatch</b> member to some other value.


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
None supported

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2012

</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in NDIS 6.30 and later.

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="netvista.ndk_cq_dispatch">NDK_CQ_DISPATCH</a>
</dt>
<dt>
<a href="netvista.ndk_object_header">NDK_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_close_object.md">NDK_FN_CLOSE_OBJECT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_create_completion.md">NDK_FN_CREATE_COMPLETION</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_create_cq.md">NDK_FN_CREATE_CQ</a>
</dt>
<dt>
<a href="netvista.ndkpi_completion_handling_requirements">NDKPI Completion Handling Requirements</a>
</dt>
<dt>
<a href="netvista.ndkpi_object_lifetime_requirements">NDKPI Object Lifetime Requirements</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NDK_CQ structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

