---
UID: NF.ndis.NdisAllocateGenericObject
title: NdisAllocateGenericObject
author: windows-driver-content
description: Components that do not have an NDIS handle use the NdisAllocateGenericObject function to allocate a generic NDIS object.
old-location: netvista\ndisallocategenericobject.htm
ms.assetid: 166584fb-8a81-4a5b-93c9-3ad5348e15a7
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisAllocateGenericObject
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function, NdisAllocateGenericObject
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisAllocateGenericObject
req.iface: 
---

# NdisAllocateGenericObject function



## -description
<p>Components that do not have an NDIS handle use the 
  <b>NdisAllocateGenericObject</b> function to allocate a generic NDIS object.</p>


## -syntax

````
PNDIS_GENERIC_OBJECT NdisAllocateGenericObject(
   PDRIVER_OBJECT DriverObject,
   ULONG          Tag,
   USHORT         Size
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [optional]

<dd>
<p>A driver object to associate with the generic object. This parameter can be <b>NULL</b>.</p>
</dd>

### -param <i>Tag</i> 

<dd>
<p>The kernel memory tag that NDIS should use to allocate memory for the generic object.</p>
</dd>

### -param <i>Size</i> 

<dd>
<p>The amount of memory, in bytes, to reserve for the caller. This does not include the size of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff565680">NDIS_GENERIC_OBJECT</a> structure. Use the
     additional memory space for your own purposes. To access the additional memory, use 
     sizeof(NDIS_GENERIC_OBJECT) to skip over the generic object structure.</p>
</dd>
</dl>

## -returns
<p><b>NdisAllocateGenericObject</b> returns a pointer to the NDIS_GENERIC_OBJECT that it allocated. If NDIS
     failed to create the object, the return value is <b>NULL</b>.</p>

## -remarks
<p>NDIS uses a generic object to manage resources that are allocated by a component that does not
    otherwise have an NDIS handle. Such a component uses the returned generic object pointer as an NDIS
    handle in some NDIS resource allocation APIs that require an NDIS handle.</p>

<p>NDIS drivers must call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561850">NdisFreeGenericObject</a> function to
    free a generic object that was created with 
    <b>NdisAllocateGenericObject</b>.</p>

<p>NDIS uses a generic object to manage resources that are allocated by a component that does not
    otherwise have an NDIS handle. Such a component uses the returned generic object pointer as an NDIS
    handle in some NDIS resource allocation APIs that require an NDIS handle.</p>

<p>NDIS drivers must call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561850">NdisFreeGenericObject</a> function to
    free a generic object that was created with 
    <b>NdisAllocateGenericObject</b>.</p>

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
<p>Supported in NDIS 6.0 and later.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547982">Irql_Miscellaneous_Function</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff561603">NdisAllocateGenericObject</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565680">NDIS_GENERIC_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561850">NdisFreeGenericObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAllocateGenericObject function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
