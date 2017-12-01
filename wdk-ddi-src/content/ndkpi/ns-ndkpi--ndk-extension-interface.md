---
UID: NS.ndkpi._NDK_EXTENSION_INTERFACE
title: NDK_EXTENSION_INTERFACE
author: windows-driver-content
description: The NDK_EXTENSION_INTERFACE structure specifies dispatch function entry points for an NDK extension interface.
old-location: netvista\ndk_extension_interface.htm
old-project: netvista
ms.assetid: BFA8FF36-1B10-4358-8826-9D5C32F27CFF
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDK_EXTENSION_INTERFACE, NDK_EXTENSION_INTERFACE
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
req.alt-api: NDK_EXTENSION_INTERFACE
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

# NDK_EXTENSION_INTERFACE structure



## -description
<p>The <b>NDK_EXTENSION_INTERFACE</b> structure specifies dispatch function entry points for an NDK extension interface.</p>


## -syntax

````
typedef struct _NDK_EXTENSION_INTERFACE {
  const VOID *Dispatch;
} NDK_EXTENSION_INTERFACE, *PNDK_EXTENSION_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>Dispatch</b>

<dd>
<p>An entry point for an extension interface dispatch function.</p>
</dd>
</dl>

## -remarks
<p>An extension interface is identified by a GUID and represented as a pointer to an <b>NDK_EXTENSION_INTERFACE</b> function dispatch table.</p>

<p>Each NDK object contains a <a href="..\ndkpi\nc-ndkpi-ndk-fn-query-extension-interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a> function pointer in its object type-specific function dispatch table. This function allows a driver to query the extended interfaces the object type supports.</p>

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
<a href="..\ndkpi\nc-ndkpi-ndk-fn-query-extension-interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_EXTENSION_INTERFACE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
