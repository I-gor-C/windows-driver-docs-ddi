---
UID: NS.wdm._PCW_REGISTRATION_INFORMATION
title: PCW_REGISTRATION_INFORMATION
author: windows-driver-content
description: The PCW_REGISTRATION_INFORMATION structure supplies details about the provider and the counter set.
old-location: devtest\pcw_registration_information.htm
old-project: devtest
ms.assetid: f5305351-10b4-47e6-a8b6-e1a91c605ca9
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PCW_REGISTRATION_INFORMATION, PCW_REGISTRATION_INFORMATION, *PPCW_REGISTRATION_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCW_REGISTRATION_INFORMATION
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
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# PCW_REGISTRATION_INFORMATION structure



## -description
<p>The PCW_REGISTRATION_INFORMATION structure supplies details about the provider and the counter set. </p>


## -syntax

````
typedef struct _PCW_REGISTRATION_INFORMATION {
  ULONG                   Version;
  PCUNICODE_STRING        Name;
  ULONG                   CounterCount;
  PPCW_COUNTER_DESCRIPTOR Counters;
  PPCW_CALLBACK           Callback;
  PVOID                   CallbackContext;
} PCW_REGISTRATION_INFORMATION, *PPCW_REGISTRATION_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The numeric value that specifies the version of Performance Counters for Windows (PCW) that the provider supports.</p>
</dd>

### -field <b>Name</b>

<dd>
<p>A pointer to the string that contains the name of the counter set to register.</p>
</dd>

### -field <b>CounterCount</b>

<dd>
<p>The number of counters that are exposed by this registration.</p>
</dd>

### -field <b>Counters</b>

<dd>
<p>A pointer to the array that describes the counters.</p>
</dd>

### -field <b>Callback</b>

<dd>
<p>A pointer to the optional <a href="..\wdm\nc-wdm-pcw-callback.md">PcwCallback</a> function that notifies the provider about events related to this counter set.</p>
</dd>

### -field <b>CallbackContext</b>

<dd>
<p>A pointer to the callback context.  </p>
</dd>
</dl>

## -remarks
<p>The <a href="..\wdm\nf-wdm-pcwregister.md">PcwRegister</a> function takes, as a parameter, a pointer to this structure to serve as the registration handle.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h or Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-pcwregister.md">PcwRegister</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--pcw-counter-descriptor.md">PCW_COUNTER_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-pcw-callback.md">PcwCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [devtest\devtest]:%20PCW_REGISTRATION_INFORMATION structure%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
