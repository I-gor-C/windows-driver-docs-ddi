---
UID: NE.wdm._KEY_VALUE_INFORMATION_CLASS
title: KEY_VALUE_INFORMATION_CLASS
author: windows-driver-content
description: The KEY_VALUE_INFORMATION_CLASS enumeration type specifies the type of information to supply about the value of a registry key.
old-location: kernel\key_value_information_class.htm
old-project: kernel
ms.assetid: 99a34b06-3352-47a6-95bc-051a5dfdd82e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
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
req.iface: 
req.product: Windows 10 or later.
---

# KEY_VALUE_INFORMATION_CLASS enumeration



## -description
<p>The <b>KEY_VALUE_INFORMATION_CLASS</b> enumeration type specifies the type of information to supply about the value of a registry key.</p>


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
<dl>

### -field <a id="KeyValueBasicInformation"></a><a id="keyvaluebasicinformation"></a><a id="KEYVALUEBASICINFORMATION"></a><b>KeyValueBasicInformation</b>

<dd>
<p>The information is stored as a <a href="..\wdm\ns-wdm--key-value-basic-information.md">KEY_VALUE_BASIC_INFORMATION</a> structure.</p>
</dd>

### -field <a id="KeyValueFullInformation"></a><a id="keyvaluefullinformation"></a><a id="KEYVALUEFULLINFORMATION"></a><b>KeyValueFullInformation</b>

<dd>
<p>The information is stored as a <a href="..\wdm\ns-wdm--key-value-full-information.md">KEY_VALUE_FULL_INFORMATION</a> structure.</p>
</dd>

### -field <a id="KeyValuePartialInformation"></a><a id="keyvaluepartialinformation"></a><a id="KEYVALUEPARTIALINFORMATION"></a><b>KeyValuePartialInformation</b>

<dd>
<p>The information is stored as a <a href="..\wdm\ns-wdm--key-value-partial-information.md">KEY_VALUE_PARTIAL_INFORMATION</a> structure.</p>
</dd>

### -field <a id="KeyValueFullInformationAlign64"></a><a id="keyvaluefullinformationalign64"></a><a id="KEYVALUEFULLINFORMATIONALIGN64"></a><b>KeyValueFullInformationAlign64</b>

<dd>
<p>The information is stored as a <b>KEY_VALUE_FULL_INFORMATION</b> structure that is aligned to a 64-bit (that is, 8-byte) boundary in memory. If the caller-supplied buffer does not start on a 64-bit boundary, the information is stored starting at the first 64-bit boundary in the buffer.</p>
</dd>

### -field <a id="KeyValuePartialInformationAlign64"></a><a id="keyvaluepartialinformationalign64"></a><a id="KEYVALUEPARTIALINFORMATIONALIGN64"></a><b>KeyValuePartialInformationAlign64</b>

<dd>
<p>The information is stored as a <b>KEY_VALUE_PARTIAL_INFORMATION</b> structure that is aligned to a 64-bit (that is, 8-byte) boundary in memory. If the caller-supplied buffer does not start on a 64-bit boundary, the information is stored starting at the first 64-bit boundary in the buffer.</p>
</dd>

### -field <a id="MaxKeyValueInfoClass"></a><a id="maxkeyvalueinfoclass"></a><a id="MAXKEYVALUEINFOCLASS"></a><b>MaxKeyValueInfoClass</b>

<dd>
<p>The maximum value in this enumeration type.</p>
</dd>
</dl>

## -remarks
<p>Use the <b>KEY_VALUE_INFORMATION_CLASS</b> values to specify the type of data to be supplied by the <a href="..\wdm\nf-wdm-zwenumeratevaluekey.md">ZwEnumerateValueKey</a> and <a href="..\wdm\nf-wdm-zwqueryvaluekey.md">ZwQueryValueKey</a> routines.</p>

## -requirements
<table>
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
<a href="..\wdm\ns-wdm--key-value-basic-information.md">KEY_VALUE_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--key-value-full-information.md">KEY_VALUE_FULL_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--key-value-partial-information.md">KEY_VALUE_PARTIAL_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwenumeratevaluekey.md">ZwEnumerateValueKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryvaluekey.md">ZwQueryValueKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KEY_VALUE_INFORMATION_CLASS enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
