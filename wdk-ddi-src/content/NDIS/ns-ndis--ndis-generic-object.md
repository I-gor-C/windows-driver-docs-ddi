---
UID: NS.ndis._NDIS_GENERIC_OBJECT
title: NDIS_GENERIC_OBJECT
author: windows-driver-content
description: The NDIS_GENERIC_OBJECT structure defines a generic object which a software component can use to obtain an NDIS handle.
old-location: netvista\ndis_generic_object.htm
ms.assetid: 1e7af434-a6ad-44c8-a33d-adebb53b8e1d
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_GENERIC_OBJECT
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
ms.keywords: NDIS_GENERIC_OBJECT, NDIS_GENERIC_OBJECT, *PNDIS_GENERIC_OBJECT
req.iface: 
---

# NDIS_GENERIC_OBJECT structure



## -description
<p>The NDIS_GENERIC_OBJECT structure defines a generic object which a software component can use to
  obtain an NDIS handle.</p>


## -syntax

````
typedef struct _NDIS_GENERIC_OBJECT {
  NDIS_OBJECT_HEADER Header;
  PVOID              Caller;
  PVOID              CallersCaller;
  PDRIVER_OBJECT     DriverObject;
} NDIS_GENERIC_OBJECT, *PNDIS_GENERIC_OBJECT;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     generic object structure (NDIS_GENERIC_OBJECT). NDIS sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_GENERIC_OBJECT, the 
     <b>Revision</b> member to NDIS_GENERIC_OBJECT_REVISION_1, and the 
     <b>Size</b> member to 
     sizeof(NDIS_GENERIC_OBJECT).</p>
</dd>

### -field <b>Caller</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>CallersCaller</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>DriverObject</b>

<dd>
<p>The driver object that is associated with the generic object. If there is no driver object, this
     member is <b>NULL</b>. This is the value passed at the 
     <i>DriverObject</i> parameter of the 
     <a href="https://msdn.microsoft.com/166584fb-8a81-4a5b-93c9-3ad5348e15a7">
     NdisAllocateGenericObject</a> function.</p>
</dd>
</dl>

## -remarks
<p>Software components that do not already have an NDIS handle call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561603">NdisAllocateGenericObject</a> to
    create a generic object. Such components use the handle obtained from 
    <b>NdisAllocateGenericObject</b> to allocate NDIS resources.</p>

<p>The 
    <i>Size</i> parameter of 
    <b>NdisAllocateGenericObject</b> specifies an amount of memory, in bytes, to reserve for the caller. 
    <b>NdisAllocateGenericObject</b> adds the additional memory after the NDIS_OBJECT_STRUCTURE members.</p>

<p>Most NDIS drivers do not require a generic object to get a handle. NDIS protocol, intermediate, and
    miniport drivers obtain a handle during initialization.</p>

<p>Use the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561850">NdisFreeGenericObject</a> function to
    free a generic object that was created with 
    <b>NdisAllocateGenericObject</b>.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561603">NdisAllocateGenericObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561850">NdisFreeGenericObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_GENERIC_OBJECT structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
