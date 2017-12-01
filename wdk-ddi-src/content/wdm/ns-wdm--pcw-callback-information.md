---
UID: NS.wdm._PCW_CALLBACK_INFORMATION
title: PCW_CALLBACK_INFORMATION
author: windows-driver-content
description: The PCW_CALLBACK_INFORMATION union supplies details about the notification to send. A provider passes a pointer to this union as a parameter to the PcwCallback function.
old-location: devtest\pcw_callback_information.htm
old-project: devtest
ms.assetid: cc1882a9-eba7-494c-9047-5c97b1e3c19b
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PCW_CALLBACK_INFORMATION, PCW_CALLBACK_INFORMATION, *PPCW_CALLBACK_INFORMATION
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
req.alt-api: PCW_CALLBACK_INFORMATION
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

# PCW_CALLBACK_INFORMATION structure



## -description
<p>The <b>PCW_CALLBACK_INFORMATION</b> union supplies details about the notification to send. A provider passes a pointer to this union as a parameter to the <a href="..\wdm\nc-wdm-pcw-callback.md">PcwCallback</a> function. </p>


## -syntax

````
typedef union _PCW_CALLBACK_INFORMATION {
  PCW_COUNTER_INFORMATION AddCounter;
  PCW_COUNTER_INFORMATION RemoveCounter;
  PCW_MASK_INFORMATION    EnumerateInstances;
  PCW_MASK_INFORMATION    CollectData;
} PCW_CALLBACK_INFORMATION, *PPCW_CALLBACK_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>AddCounter</b>

<dd>
<p>The PCW_COUNTER_INFORMATION structure that identifies the counter being added. </p>
</dd>

### -field <b>RemoveCounter</b>

<dd>
<p>The PCW_COUNTER_INFORMATION structure that identifies the counter being removed. </p>
</dd>

### -field <b>EnumerateInstances</b>

<dd>
<p>The PCW_MASK_INFORMATION structure that identifies the instances of the counter set.</p>
</dd>

### -field <b>CollectData</b>

<dd>
<p>The PCW_MASK_INFORMATION structure that identifies the instance of the counter set and its buffer.</p>
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
<a href="..\wdm\ns-wdm--pcw-counter-information.md">PCW_COUNTER_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--pcw-mask-information.md">PCW_MASK_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [devtest\devtest]:%20PCW_CALLBACK_INFORMATION union%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
