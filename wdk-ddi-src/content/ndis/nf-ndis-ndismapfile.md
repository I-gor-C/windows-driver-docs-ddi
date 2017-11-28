---
UID: NF.ndis.NdisMapFile
title: NdisMapFile
author: windows-driver-content
description: The NdisMapFile function maps an already open file into a caller-accessible buffer if the file is currently unmapped.
old-location: netvista\ndismapfile.htm
old-project: netvista
ms.assetid: 965bb4c7-826d-425b-b10d-2d5a29ca0f91
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMapFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisMapFile (NDIS 5.1)) in Windows
   Vista. Supported for NDIS 5.1 drivers (see 
   NdisMapFile (NDIS 5.1)) in Windows
   XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMapFile
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisMapFile function



## -description
<p>The 
  <b>NdisMapFile</b> function maps an already open file into a caller-accessible buffer if the file is
  currently unmapped.</p>


## -syntax

````
VOID NdisMapFile(
  _Out_ PNDIS_STATUS Status,
  _Out_ PVOID *      MappedBuffer,
  _In_  NDIS_HANDLE  FileHandle
);
````


## -parameters
<dl>

### -param <i>Status</i> [out]

<dd>
<p>A pointer to a caller-supplied variable in which this function returns the status of the mapping
     operation, which can be one of the following:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>The caller has exclusive access to the file contents until the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff564641">NdisUnmapFile</a> function is called.</p>
</dd>

### -param <a id="NDIS_STATUS_ALREADY_MAPPED"></a><a id="ndis_status_already_mapped"></a>NDIS_STATUS_ALREADY_MAPPED

<dd>
<p>The caller cannot access the file contents at this time.</p>
</dd>
</dl>
</dd>

### -param <i>MappedBuffer</i> [out]

<dd>
<p>A pointer to a caller-supplied variable in which this function returns the base virtual address of
     the mapped file contents or <b>NULL</b>.</p>
</dd>

### -param <i>FileHandle</i> [in]

<dd>
<p>The handle that was returned by a preceding call to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563728">NdisOpenFile</a> function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisMapFile</b> associates (maps) a virtual address range with an opened file so the driver can access
    the file contents. 
    <b>NdisMapFile</b> allows only one mapping of a particular file to be outstanding at any time.
    Consequently, a successful caller is given exclusive access to the file data until 
    <b>NdisUnmapFile</b> or the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561645">NdisCloseFile</a> function is called.</p>

<p>A miniport driver can map and unmap such an open file as necessary, using alternating calls to 
    <b>NdisMapFile</b> and 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564641">NdisUnmapFile</a>. A call to 
    <b>NdisCloseFile</b> releases the 
    <i>FileHandle</i> and deallocates the buffer containing the file contents.</p>

<p>A miniport driver can call 
    <b>NdisMapFile</b> only during initialization.</p>

<p><b>NdisMapFile</b> associates (maps) a virtual address range with an opened file so the driver can access
    the file contents. 
    <b>NdisMapFile</b> allows only one mapping of a particular file to be outstanding at any time.
    Consequently, a successful caller is given exclusive access to the file data until 
    <b>NdisUnmapFile</b> or the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561645">NdisCloseFile</a> function is called.</p>

<p>A miniport driver can map and unmap such an open file as necessary, using alternating calls to 
    <b>NdisMapFile</b> and 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564641">NdisUnmapFile</a>. A call to 
    <b>NdisCloseFile</b> releases the 
    <i>FileHandle</i> and deallocates the buffer containing the file contents.</p>

<p>A miniport driver can call 
    <b>NdisMapFile</b> only during initialization.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff552308">NdisMapFile (NDIS 5.1)</a>) in Windows
   Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMapFile (NDIS 5.1)</b>) in Windows
   XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547982">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561645">NdisCloseFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563728">NdisOpenFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564641">NdisUnmapFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMapFile function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
