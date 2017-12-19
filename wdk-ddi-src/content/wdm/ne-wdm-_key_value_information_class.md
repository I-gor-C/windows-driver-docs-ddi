---
UID: NE.wdm._KEY_VALUE_INFORMATION_CLASS
title: _KEY_VALUE_INFORMATION_CLASS
author: windows-driver-content
description: The KEY_VALUE_INFORMATION_CLASS enumeration type specifies the type of information to supply about the value of a registry key.
old-location: kernel\key_value_information_class.htm
old-project: kernel
ms.assetid: 99a34b06-3352-47a6-95bc-051a5dfdd82e
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _KEY_VALUE_INFORMATION_CLASS, KEY_VALUE_INFORMATION_CLASS
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
req.alt-api: KEY_VALUE_INFORMATION_CLASS
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
req.product: Windows 10 or later.
---

# _KEY_VALUE_INFORMATION_CLASS enumeration



## -description
The <b>KEY_VALUE_INFORMATION_CLASS</b> enumeration type specifies the type of information to supply about the value of a registry key.



## -syntax

````
typedef enum _KEY_VALUE_INFORMATION_CLASS { 
  KeyValueBasicInformation           = 0,
  KeyValueFullInformation,
  KeyValuePartialInformation,
  KeyValueFullInformationAlign64,
  KeyValuePartialInformationAlign64,
  MaxKeyValueInfoClass
} KEY_VALUE_INFORMATION_CLASS;
````


## -enum-fields

### -field KeyValueBasicInformation

The information is stored as a <a href="kernel.key_value_basic_information">KEY_VALUE_BASIC_INFORMATION</a> structure.


### -field KeyValueFullInformation

The information is stored as a <a href="kernel.key_value_full_information">KEY_VALUE_FULL_INFORMATION</a> structure.


### -field KeyValuePartialInformation

The information is stored as a <a href="kernel.key_value_partial_information">KEY_VALUE_PARTIAL_INFORMATION</a> structure.


### -field KeyValueFullInformationAlign64

The information is stored as a <b>KEY_VALUE_FULL_INFORMATION</b> structure that is aligned to a 64-bit (that is, 8-byte) boundary in memory. If the caller-supplied buffer does not start on a 64-bit boundary, the information is stored starting at the first 64-bit boundary in the buffer.


### -field KeyValuePartialInformationAlign64

The information is stored as a <b>KEY_VALUE_PARTIAL_INFORMATION</b> structure that is aligned to a 64-bit (that is, 8-byte) boundary in memory. If the caller-supplied buffer does not start on a 64-bit boundary, the information is stored starting at the first 64-bit boundary in the buffer.


### -field MaxKeyValueInfoClass

The maximum value in this enumeration type.


## -remarks
Use the <b>KEY_VALUE_INFORMATION_CLASS</b> values to specify the type of data to be supplied by the <a href="kernel.zwenumeratevaluekey">ZwEnumerateValueKey</a> and <a href="kernel.zwqueryvaluekey">ZwQueryValueKey</a> routines.


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
<a href="kernel.key_value_basic_information">KEY_VALUE_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="kernel.key_value_full_information">KEY_VALUE_FULL_INFORMATION</a>
</dt>
<dt>
<a href="kernel.key_value_partial_information">KEY_VALUE_PARTIAL_INFORMATION</a>
</dt>
<dt>
<a href="kernel.zwenumeratevaluekey">ZwEnumerateValueKey</a>
</dt>
<dt>
<a href="kernel.zwqueryvaluekey">ZwQueryValueKey</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KEY_VALUE_INFORMATION_CLASS enumeration%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

