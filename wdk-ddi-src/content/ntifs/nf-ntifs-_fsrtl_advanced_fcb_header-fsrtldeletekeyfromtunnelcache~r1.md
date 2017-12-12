---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlDeleteKeyFromTunnelCache~r1
title: FsRtlDeleteKeyFromTunnelCache function
author: windows-driver-content
description: The FsRtlDeleteKeyFromTunnelCache routine deletes any tunnel cache entries for files in a directory that is being deleted.
old-location: ifsk\fsrtldeletekeyfromtunnelcache.htm
old-project: ifsk
ms.assetid: 01f0d1ab-7c7f-4ee2-89f0-c48b257bafbb
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlDeleteKeyFromTunnelCache
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 and later versions of Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlDeleteKeyFromTunnelCache
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
---

# FsRtlDeleteKeyFromTunnelCache function



## -description
The <b>FsRtlDeleteKeyFromTunnelCache</b> routine deletes any tunnel cache entries for files in a directory that is being deleted.



## -syntax

````
VOID FsRtlDeleteKeyFromTunnelCache(
  _In_ TUNNEL    *Cache,
  _In_ ULONGLONG DirKey
);
````


## -parameters

### -param Cache [in]

A pointer to a tunnel cache that was initialized by <a href="ifsk.fsrtlinitializetunnelcache">FsRtlInitializeTunnelCache</a>.


### -param DirKey [in]

The directory key value for the directory that is being removed. For more information, see the reference entry for <a href="ifsk.fsrtlinitializetunnelcache">FsRtlInitializeTunnelCache</a>.


## -returns
None


## -remarks
File systems call <b>FsRtlDeleteKeyFromTunnelCache</b> when deleting a directory from a volume. <b>FsRtlDeleteKeyFromTunnelCache</b> deletes all tunnel cache entries whose directory keys match the value specified in the <i>DirKey</i> parameter. 

To delete the tunnel cache, use <a href="ifsk.fsrtldeletetunnelcache">FsRtlDeleteTunnelCache</a>.

The caller is required to synchronize this call against <a href="ifsk.fsrtldeletetunnelcache">FsRtlDeleteTunnelCache</a>. In other words, a file system must ensure that it does not call <b>FsRtlDeleteKeyFromTunnelCache</b> and <b>FsRtlDeleteTunnelCache</b> at the same time from different threads. 

For more information about file name tunneling, see <a href="http://go.microsoft.com/fwlink/p/?linkid=3100&amp;amp;id=172190">Microsoft Knowledge Base Article 172190</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
This routine is available on Microsoft Windows 2000 and later versions of Windows operating systems. 

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsrtldeletetunnelcache">FsRtlDeleteTunnelCache</a>
</dt>
<dt>
<a href="ifsk.fsrtlinitializetunnelcache">FsRtlInitializeTunnelCache</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlDeleteKeyFromTunnelCache routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

