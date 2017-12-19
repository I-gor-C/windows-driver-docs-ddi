---
UID: NE.wdm._KEY_INFORMATION_CLASS
title: _KEY_INFORMATION_CLASS
author: windows-driver-content
description: The KEY_INFORMATION_CLASS enumeration type represents the type of information to supply about a registry key.
old-location: kernel\key_information_class.htm
old-project: kernel
ms.assetid: cb531a0e-c934-4f3e-9b92-07eb3ab75673
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _KEY_INFORMATION_CLASS, KEY_INFORMATION_CLASS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KEY_INFORMATION_CLASS
req.alt-loc: wdm.h
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
req.product: Windows 10 or later.
---

# _KEY_INFORMATION_CLASS enumeration



## -description
The <b>KEY_INFORMATION_CLASS</b> enumeration type represents the type of information to supply about a registry key.



## -syntax

````
typedef enum _KEY_INFORMATION_CLASS { 
  KeyBasicInformation           = 0,
  KeyNodeInformation            = 1,
  KeyFullInformation            = 2,
  KeyNameInformation            = 3,
  KeyCachedInformation          = 4,
  KeyFlagsInformation           = 5,
  KeyVirtualizationInformation  = 6,
  KeyHandleTagsInformation      = 7,
  MaxKeyInfoClass               = 8
} KEY_INFORMATION_CLASS;
````


## -enum-fields

### -field KeyBasicInformation

A <a href="kernel.key_basic_information">KEY_BASIC_INFORMATION</a> structure is supplied.


### -field KeyNodeInformation

A <a href="kernel.key_node_information">KEY_NODE_INFORMATION</a> structure is supplied.


### -field KeyFullInformation

A <a href="kernel.key_full_information">KEY_FULL_INFORMATION</a> structure is supplied.


### -field KeyNameInformation

A <a href="kernel.key_name_information">KEY_NAME_INFORMATION</a> structure is supplied.


### -field KeyCachedInformation

A <a href="kernel.key_cached_information">KEY_CACHED_INFORMATION</a> structure is supplied.


### -field KeyFlagsInformation

Reserved for system use.


### -field KeyVirtualizationInformation

A <a href="kernel.key_virtualization_information">KEY_VIRTUALIZATION_INFORMATION</a> structure is supplied.


### -field KeyHandleTagsInformation

Reserved for system use.


### -field MaxKeyInfoClass

The maximum value in this enumeration type.


## -remarks
Use the <b>KEY_INFORMATION_CLASS</b> values to specify the type of data to be supplied by the <a href="kernel.zwenumeratekey">ZwEnumerateKey</a> and <a href="kernel.zwquerykey">ZwQueryKey</a> routines.


## -requirements
<table>
<tr>
<th width="30%">
Header

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
<a href="kernel.key_basic_information">KEY_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="kernel.key_cached_information">KEY_CACHED_INFORMATION</a>
</dt>
<dt>
<a href="kernel.key_full_information">KEY_FULL_INFORMATION</a>
</dt>
<dt>
<a href="kernel.key_name_information">KEY_NAME_INFORMATION</a>
</dt>
<dt>
<a href="kernel.key_node_information">KEY_NODE_INFORMATION</a>
</dt>
<dt>
<a href="kernel.key_virtualization_information">KEY_VIRTUALIZATION_INFORMATION</a>
</dt>
<dt>
<a href="kernel.zwenumeratekey">ZwEnumerateKey</a>
</dt>
<dt>
<a href="kernel.zwquerykey">ZwQueryKey</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KEY_INFORMATION_CLASS enumeration%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

