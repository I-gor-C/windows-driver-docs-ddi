---
UID: NS.ndkpi._NDK_OBJECT_HEADER
title: NDK_OBJECT_HEADER
author: windows-driver-content
description: The NDK_OBJECT_HEADER structure specifies the object version, type, and other information. It is used in the Header member of every NDK object.
old-location: netvista\ndk_object_header.htm
old-project: netvista
ms.assetid: 12E3ED4A-F078-4489-BC84-69EE735CAEF8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDK_OBJECT_HEADER, NDK_OBJECT_HEADER
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
req.iface: 
---

# NDK_OBJECT_HEADER structure



## -description
<p>The <b>NDK_OBJECT_HEADER</b> structure specifies the object version, type, and other  information.

It is used in the <b>Header</b> member of every NDK object.</p>


## -syntax

````
typedef struct _NDK_OBJECT_HEADER {
  NDK_VERSION                      Version;
  NDK_OBJECT_TYPE                  ObjectType;
  NDK_OBJECT_HEADER_RESERVED_BLOCK NdkReserved;
} NDK_OBJECT_HEADER, *PNDK_OBJECT_HEADER;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/hh439942">NDK_VERSION</a> structure that contains the revision number of the NDK object.</p>
</dd>

### -field <b>ObjectType</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/hh439930">NDK_OBJECT_TYPE</a> enumeration value that specifies the NDK object type. You can use this member to identify an NDK object's type in a memory dump.

This member is required and cannot be zero.</p>
</dd>

### -field <b>NdkReserved</b>

<dd>
<p>A reserved block in an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439929">NDK_OBJECT_HEADER_RESERVED_BLOCK</a> structure.</p>
</dd>
</dl>

## -remarks
<p>When an NDK provider creates an NDK object instance, the <b>Header</b> member must be initialized as follows:</p>

<p>For Windows Server 2012, set the <b>Version</b> member to 1.1. To do this, set both the <b>Major</b> and <b>Minor</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439942">NDK_VERSION</a> structure to 1.</p>

<p>For Windows Server 2012 R2, set the <b>Version</b> member to 1.2. To do this, set the <b>Major</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439942">NDK_VERSION</a> structure to 1 and the <b>Minor</b> member to 2.</p>

<p>Set the <b>ObjectType</b>  member to an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439930">NDK_OBJECT_TYPE</a> value.</p>

<p>Set the  <b>NdkReserved</b> member to zero. The NDK provider must not modify this member until the object is closed.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439852">NDK_CONNECTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439854">NDK_CQ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439918">NDK_LISTENER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439922">NDK_MR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439926">NDK_MW</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439929">NDK_OBJECT_HEADER_RESERVED_BLOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439930">NDK_OBJECT_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439931">NDK_PD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439933">NDK_QP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439939">NDK_SRQ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439942">NDK_VERSION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439871">NDK_FN_CREATE_COMPLETION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439901">NDK_FN_INVALIDATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_OBJECT_HEADER structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
