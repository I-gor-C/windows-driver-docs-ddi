---
UID: NS.NDKPI._NDK_OBJECT_HEADER
title: _NDK_OBJECT_HEADER
author: windows-driver-content
description: The NDK_OBJECT_HEADER structure specifies the object version, type, and other information. It is used in the Header member of every NDK object.
old-location: netvista\ndk_object_header.htm
old-project: netvista
ms.assetid: 12E3ED4A-F078-4489-BC84-69EE735CAEF8
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _NDK_OBJECT_HEADER, NDK_OBJECT_HEADER
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
req.alt-api: NDK_OBJECT_HEADER
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

# _NDK_OBJECT_HEADER structure



## -description
The <b>NDK_OBJECT_HEADER</b> structure specifies the object version, type, and other  information.

It is used in the <b>Header</b> member of every NDK object.



## -syntax

````
typedef struct _NDK_OBJECT_HEADER {
  NDK_VERSION                      Version;
  NDK_OBJECT_TYPE                  ObjectType;
  NDK_OBJECT_HEADER_RESERVED_BLOCK NdkReserved;
} NDK_OBJECT_HEADER, *PNDK_OBJECT_HEADER;
````


## -struct-fields

### -field Version

An <a href="netvista.ndk_version">NDK_VERSION</a> structure that contains the revision number of the NDK object.


### -field ObjectType

An <a href="netvista.ndk_object_type">NDK_OBJECT_TYPE</a> enumeration value that specifies the NDK object type. You can use this member to identify an NDK object's type in a memory dump.

This member is required and cannot be zero.


### -field NdkReserved

A reserved block in an <a href="netvista.ndk_object_header_reserved_block">NDK_OBJECT_HEADER_RESERVED_BLOCK</a> structure.


## -remarks
When an NDK provider creates an NDK object instance, the <b>Header</b> member must be initialized as follows:

For Windows Server 2012, set the <b>Version</b> member to 1.1. To do this, set both the <b>Major</b> and <b>Minor</b> members of the <a href="netvista.ndk_version">NDK_VERSION</a> structure to 1.

For Windows Server 2012 R2, set the <b>Version</b> member to 1.2. To do this, set the <b>Major</b> member of the <a href="netvista.ndk_version">NDK_VERSION</a> structure to 1 and the <b>Minor</b> member to 2.

Set the <b>ObjectType</b>  member to an <a href="netvista.ndk_object_type">NDK_OBJECT_TYPE</a> value.

Set the  <b>NdkReserved</b> member to zero. The NDK provider must not modify this member until the object is closed.


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
<a href="netvista.ndk_adapter">NDK_ADAPTER</a>
</dt>
<dt>
<a href="netvista.ndk_connector">NDK_CONNECTOR</a>
</dt>
<dt>
<a href="netvista.ndk_cq">NDK_CQ</a>
</dt>
<dt>
<a href="netvista.ndk_listener">NDK_LISTENER</a>
</dt>
<dt>
<a href="netvista.ndk_mr">NDK_MR</a>
</dt>
<dt>
<a href="netvista.ndk_mw">NDK_MW</a>
</dt>
<dt>
<a href="netvista.ndk_object_header_reserved_block">NDK_OBJECT_HEADER_RESERVED_BLOCK</a>
</dt>
<dt>
<a href="netvista.ndk_object_type">NDK_OBJECT_TYPE</a>
</dt>
<dt>
<a href="netvista.ndk_pd">NDK_PD</a>
</dt>
<dt>
<a href="netvista.ndk_qp">NDK_QP</a>
</dt>
<dt>
<a href="netvista.ndk_shared_endpoint">NDK_SHARED_ENDPOINT</a>
</dt>
<dt>
<a href="netvista.ndk_srq">NDK_SRQ</a>
</dt>
<dt>
<a href="netvista.ndk_version">NDK_VERSION</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_close_object.md">NDK_FN_CLOSE_OBJECT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_create_completion.md">NDK_FN_CREATE_COMPLETION</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_invalidate.md">NDK_FN_INVALIDATE</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk_fn_query_extension_interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_OBJECT_HEADER structure%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

