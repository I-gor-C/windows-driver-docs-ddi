---
UID: NE.wdm._KTMOBJECT_TYPE
title: KTMOBJECT_TYPE
author: windows-driver-content
description: The KTMOBJECT_TYPE enumeration identifies the types of objects that KTM supports.
old-location: kernel\ktmobject_type.htm
old-project: kernel
ms.assetid: 0ace1cdf-0a15-48bb-9444-c947239e453e
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
req.alt-api: KTMOBJECT_TYPE
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

# KTMOBJECT_TYPE enumeration



## -description
<p>The <b>KTMOBJECT_TYPE</b> enumeration identifies the types of objects that KTM supports.</p>


## -syntax

````
typedef enum _KTMOBJECT_TYPE { 
  KTMOBJECT_TRANSACTION          = 0,
  KTMOBJECT_TRANSACTION_MANAGER  = 1,
  KTMOBJECT_RESOURCE_MANAGER     = 2,
  KTMOBJECT_ENLISTMENT           = 3,
  KTMOBJECT_INVALID              = 4
} KTMOBJECT_TYPE, *PKTMOBJECT_TYPE;
````


## -enum-fields
<dl>

### -field KTMOBJECT_TRANSACTION

<dd>
<p>KTM transaction objects.</p>
</dd>

### -field KTMOBJECT_TRANSACTION_MANAGER

<dd>
<p>KTM transaction manager objects.</p>
</dd>

### -field KTMOBJECT_RESOURCE_MANAGER

<dd>
<p>KTM resource manager objects.</p>
</dd>

### -field KTMOBJECT_ENLISTMENT

<dd>
<p>KTM enlistment objects.</p>
</dd>

### -field KTMOBJECT_INVALID

<dd>
<p>Invalid object type.</p>
</dd>
</dl>

## -remarks
<p>The <b>KTMOBJECT_TYPE</b> enumeration is used with the <a href="..\wdm\nf-wdm-zwenumeratetransactionobject.md">ZwEnumerateTransactionObject</a> routine.</p>

<p>For more information about KTM objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554272">KTM Objects</a>.</p>

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
<a href="..\wdm\nf-wdm-zwenumeratetransactionobject.md">ZwEnumerateTransactionObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KTMOBJECT_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
