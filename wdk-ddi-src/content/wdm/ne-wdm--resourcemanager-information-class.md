---
UID: NE.wdm._RESOURCEMANAGER_INFORMATION_CLASS
title: RESOURCEMANAGER_INFORMATION_CLASS
author: windows-driver-content
description: The RESOURCEMANAGER_INFORMATION_CLASS enumeration identifies the type of information that the ZwQueryInformationResourceManager routine can retrieve for a resource manager object.
old-location: kernel\resourcemanager_information_class.htm
old-project: kernel
ms.assetid: 5ffaad89-b3c0-4fe6-bc2c-2b1f3b1bcfd2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later operating system versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RESOURCEMANAGER_INFORMATION_CLASS
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# RESOURCEMANAGER_INFORMATION_CLASS enumeration



## -description
<p>The <b>RESOURCEMANAGER_INFORMATION_CLASS</b> enumeration identifies the type of information that the <a href="..\wdm\nf-wdm-zwqueryinformationresourcemanager.md">ZwQueryInformationResourceManager</a> routine can retrieve for a <a href="https://msdn.microsoft.com/b44f2035-ee9f-453b-b12d-89ca36a8b280">resource manager object</a>.</p>


## -syntax

````
typedef enum _RESOURCEMANAGER_INFORMATION_CLASS { 
  ResourceManagerBasicInformation       = 0,
  ResourceManagerCompletionInformation  = 1
} RESOURCEMANAGER_INFORMATION_CLASS;
````


## -enum-fields
<dl>

### -field ResourceManagerBasicInformation

<dd>
<p>Information about a resource manager object is stored in a <a href="..\wdm\ns-wdm--resourcemanager-basic-information.md">RESOURCEMANAGER_BASIC_INFORMATION</a> structure. </p>
</dd>

### -field ResourceManagerCompletionInformation

<dd>
<p>Information about a resource manager object is stored in a <a href="..\wdm\ns-wdm--resourcemanager-completion-information.md">RESOURCEMANAGER_COMPLETION_INFORMATION</a> structure. </p>
</dd>
</dl>

## -remarks


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
<a href="..\wdm\ns-wdm--resourcemanager-basic-information.md">RESOURCEMANAGER_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--resourcemanager-completion-information.md">RESOURCEMANAGER_COMPLETION_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryinformationresourcemanager.md">ZwQueryInformationResourceManager</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RESOURCEMANAGER_INFORMATION_CLASS enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
