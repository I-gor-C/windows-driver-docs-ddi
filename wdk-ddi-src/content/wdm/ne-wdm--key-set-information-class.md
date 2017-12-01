---
UID: NE.wdm._KEY_SET_INFORMATION_CLASS
title: KEY_SET_INFORMATION_CLASS
author: windows-driver-content
description: The KEY_SET_INFORMATION_CLASS enumeration type represents the type of information to set for a registry key.
old-location: kernel\key_set_information_class.htm
old-project: kernel
ms.assetid: 95a8f683-642c-4f33-9536-08f497567f87
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KEY_SET_INFORMATION_CLASS
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

# KEY_SET_INFORMATION_CLASS enumeration



## -description
<p>The <b>KEY_SET_INFORMATION_CLASS</b> enumeration type represents the type of information to set for a registry key.</p>


## -syntax

````
typedef enum _KEY_SET_INFORMATION_CLASS { 
  KeyWriteTimeInformation,
  KeyWow64FlagsInformation,
  KeyControlFlagsInformation,
  KeySetVirtualizationInformation,
  KeySetDebugInformation,
  KeySetHandleTagsInformation,
  MaxKeySetInfoClass
} KEY_SET_INFORMATION_CLASS;
````


## -enum-fields
<dl>

### -field <a id="KeyWriteTimeInformation"></a><a id="keywritetimeinformation"></a><a id="KEYWRITETIMEINFORMATION"></a><b>KeyWriteTimeInformation</b>

<dd>
<p>Indicates that a <a href="..\wdm\ns-wdm--key-write-time-information.md">KEY_WRITE_TIME_INFORMATION</a> structure is supplied.</p>
</dd>

### -field <a id="KeyWow64FlagsInformation"></a><a id="keywow64flagsinformation"></a><a id="KEYWOW64FLAGSINFORMATION"></a><b>KeyWow64FlagsInformation</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="KeyControlFlagsInformation"></a><a id="keycontrolflagsinformation"></a><a id="KEYCONTROLFLAGSINFORMATION"></a><b>KeyControlFlagsInformation</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="KeySetVirtualizationInformation"></a><a id="keysetvirtualizationinformation"></a><a id="KEYSETVIRTUALIZATIONINFORMATION"></a><b>KeySetVirtualizationInformation</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="KeySetDebugInformation"></a><a id="keysetdebuginformation"></a><a id="KEYSETDEBUGINFORMATION"></a><b>KeySetDebugInformation</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="KeySetHandleTagsInformation"></a><a id="keysethandletagsinformation"></a><a id="KEYSETHANDLETAGSINFORMATION"></a><b>KeySetHandleTagsInformation</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="MaxKeySetInfoClass"></a><a id="maxkeysetinfoclass"></a><a id="MAXKEYSETINFOCLASS"></a><b>MaxKeySetInfoClass</b>

<dd>
<p>This member constant is always the maximum value in the enumeration.</p>
</dd>
</dl>

## -remarks
<p>A <a href="kernel.registrycallback">RegistryCallback</a> routine can receive a pointer to a <b>KEY_SET_INFORMATION_CLASS</b> structure as an input parameter.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows XP.</p>
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
<a href="..\wdm\ns-wdm--key-write-time-information.md">KEY_WRITE_TIME_INFORMATION</a>
</dt>
<dt>
<a href="kernel.registrycallback">RegistryCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KEY_SET_INFORMATION_CLASS enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
