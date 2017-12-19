---
UID: NE.wwan._WWAN_SMS_FLAG
title: _WWAN_SMS_FLAG
author: windows-driver-content
description: The WWAN_SMS_FLAG enumeration lists different flags to filter SMS text messages.
old-location: netvista\wwan_sms_flag.htm
old-project: NetVista
ms.assetid: 6620d6c8-2b8a-440e-acf4-fb08570b13bf
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _WWAN_SMS_FLAG, PWWAN_SMS_FLAG, WWAN_SMS_FLAG, *PWWAN_SMS_FLAG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_SMS_FLAG
req.alt-loc: wwan.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# _WWAN_SMS_FLAG enumeration



## -description
The WWAN_SMS_FLAG enumeration lists different flags to filter SMS text messages.



## -syntax

````
typedef enum _WWAN_SMS_FLAG { 
  WwanSmsFlagAll    = 0,
  WwanSmsFlagIndex,
  WwanSmsFlagNew,
  WwanSmsFlagOld,
  WwanSmsFlagSent,
  WwanSmsFlagDraft,
  WwanSmsFlagMax
} WWAN_SMS_FLAG, *PWWAN_SMS_FLAG;
````


## -enum-fields

### -field WwanSmsFlagAll

No filter is set.


### -field WwanSmsFlagIndex

Filter based on the value of an index.


### -field WwanSmsFlagNew

Filter for new (unread) messages.


### -field WwanSmsFlagOld

Filter for old (read) messages.


### -field WwanSmsFlagSent

Filter for sent messages.


### -field WwanSmsFlagDraft

Filter for draft messages.


### -field WwanSmsFlagMax

The total number of filter flags.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows 7 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.wwan_sms_filter">WWAN_SMS_FILTER</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20WWAN_SMS_FLAG enumeration%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

