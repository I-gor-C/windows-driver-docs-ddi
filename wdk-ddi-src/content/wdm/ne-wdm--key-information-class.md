---
UID: NE.wdm._KEY_INFORMATION_CLASS
title: KEY_INFORMATION_CLASS
author: windows-driver-content
description: The KEY_INFORMATION_CLASS enumeration type represents the type of information to supply about a registry key.
old-location: kernel\key_information_class.htm
old-project: kernel
ms.assetid: cb531a0e-c934-4f3e-9b92-07eb3ab75673
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
req.iface: 
req.product: Windows 10 or later.
---

# KEY_INFORMATION_CLASS enumeration



## -description
<p>The <b>KEY_INFORMATION_CLASS</b> enumeration type represents the type of information to supply about a registry key.</p>


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
<dl>

### -field <a id="KeyBasicInformation"></a><a id="keybasicinformation"></a><a id="KEYBASICINFORMATION"></a><b>KeyBasicInformation</b>

<dd>
<p>A <a href="..\wdm\ns-wdm--key-basic-information.md">KEY_BASIC_INFORMATION</a> structure is supplied.</p>
</dd>

### -field <a id="KeyNodeInformation"></a><a id="keynodeinformation"></a><a id="KEYNODEINFORMATION"></a><b>KeyNodeInformation</b>

<dd>
<p>A <a href="..\wdm\ns-wdm--key-node-information.md">KEY_NODE_INFORMATION</a> structure is supplied.</p>
</dd>

### -field <a id="KeyFullInformation"></a><a id="keyfullinformation"></a><a id="KEYFULLINFORMATION"></a><b>KeyFullInformation</b>

<dd>
<p>A <a href="..\wdm\ns-wdm--key-full-information.md">KEY_FULL_INFORMATION</a> structure is supplied.</p>
</dd>

### -field <a id="KeyNameInformation"></a><a id="keynameinformation"></a><a id="KEYNAMEINFORMATION"></a><b>KeyNameInformation</b>

<dd>
<p>A <a href="..\ntddk\ns-ntddk--key-name-information.md">KEY_NAME_INFORMATION</a> structure is supplied.</p>
</dd>

### -field <a id="KeyCachedInformation"></a><a id="keycachedinformation"></a><a id="KEYCACHEDINFORMATION"></a><b>KeyCachedInformation</b>

<dd>
<p>A <a href="..\ntddk\ns-ntddk--key-cached-information.md">KEY_CACHED_INFORMATION</a> structure is supplied.</p>
</dd>

### -field <a id="KeyFlagsInformation"></a><a id="keyflagsinformation"></a><a id="KEYFLAGSINFORMATION"></a><b>KeyFlagsInformation</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="KeyVirtualizationInformation"></a><a id="keyvirtualizationinformation"></a><a id="KEYVIRTUALIZATIONINFORMATION"></a><b>KeyVirtualizationInformation</b>

<dd>
<p>A <a href="..\ntddk\ns-ntddk--key-virtualization-information.md">KEY_VIRTUALIZATION_INFORMATION</a> structure is supplied.</p>
</dd>

### -field <a id="KeyHandleTagsInformation"></a><a id="keyhandletagsinformation"></a><a id="KEYHANDLETAGSINFORMATION"></a><b>KeyHandleTagsInformation</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="MaxKeyInfoClass"></a><a id="maxkeyinfoclass"></a><a id="MAXKEYINFOCLASS"></a><b>MaxKeyInfoClass</b>

<dd>
<p>The maximum value in this enumeration type.</p>
</dd>
</dl>

## -remarks
<p>Use the <b>KEY_INFORMATION_CLASS</b> values to specify the type of data to be supplied by the <a href="..\wdm\nf-wdm-zwenumeratekey.md">ZwEnumerateKey</a> and <a href="..\wdm\nf-wdm-zwquerykey.md">ZwQueryKey</a> routines.</p>

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
<a href="..\wdm\ns-wdm--key-basic-information.md">KEY_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--key-cached-information.md">KEY_CACHED_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--key-full-information.md">KEY_FULL_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--key-name-information.md">KEY_NAME_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--key-node-information.md">KEY_NODE_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--key-virtualization-information.md">KEY_VIRTUALIZATION_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwenumeratekey.md">ZwEnumerateKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwquerykey.md">ZwQueryKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KEY_INFORMATION_CLASS enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
