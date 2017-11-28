---
UID: NS.wdm._RESOURCEMANAGER_BASIC_INFORMATION
title: RESOURCEMANAGER_BASIC_INFORMATION
author: windows-driver-content
description: The RESOURCEMANAGER_BASIC INFORMATION structure contains information about a resource manager object.
old-location: kernel\resourcemanager_basic_information.htm
old-project: kernel
ms.assetid: b5295760-7f0e-4973-9ce3-4aa35ea5211b
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RESOURCEMANAGER_BASIC_INFORMATION, RESOURCEMANAGER_BASIC_INFORMATION, *PRESOURCEMANAGER_BASIC_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later operating system versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RESOURCEMANAGER_BASIC_INFORMATION
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# RESOURCEMANAGER_BASIC_INFORMATION structure



## -description
<p>The <b>RESOURCEMANAGER_BASIC INFORMATION</b> structure contains information about a <a href="https://msdn.microsoft.com/b44f2035-ee9f-453b-b12d-89ca36a8b280">resource manager object</a>.</p>


## -syntax

````
typedef struct _RESOURCEMANAGER_BASIC_INFORMATION {
  GUID  ResourceManagerId;
  ULONG DescriptionLength;
  WCHAR Description[1];
} RESOURCEMANAGER_BASIC_INFORMATION, *PRESOURCEMANAGER_BASIC_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>ResourceManagerId</b>

<dd>
<p>A GUID that KTM assigned to the resource manager.</p>
</dd>

### -field <b>DescriptionLength</b>

<dd>
<p>The length, in bytes, of the character array that the <b>Description</b> member provides.</p>
</dd>

### -field <b>Description</b>

<dd>
<p>A caller-allocated array of characters that receives a resource manager's description string. </p>
</dd>
</dl>

## -remarks
<p>The <b>RESOURCEMANAGER_BASIC INFORMATION</b> structure is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567054">ZwQueryInformationResourceManager</a> routine.</p>

<p>The resource manager's description string, which the <b>Description</b> member receives, is the description that the resource manager previously specified when it called <a href="https://msdn.microsoft.com/library/windows/hardware/ff566427">ZwCreateResourceManager</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later operating system versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566427">ZwCreateResourceManager</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567054">ZwQueryInformationResourceManager</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RESOURCEMANAGER_BASIC_INFORMATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
