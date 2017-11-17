---
UID: NS.iscsiprf._MSiSCSI_InitiatorLoginStatistics
title: MSiSCSI_InitiatorLoginStatistics
author: windows-driver-content
description: The MSiSCSI_InitiatorLoginStatistics structure is used by iSCSI initiators to report logon statistics.
old-location: storage\msiscsi_initiatorloginstatistics.htm
ms.assetid: 8d670887-e8bb-4b99-99ae-16c0dd9c4431
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: iscsiprf.h
req.include-header: Iscsiprf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MSiSCSI_InitiatorLoginStatistics
req.alt-loc: iscsiprf.h
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
ms.keywords: MSiSCSI_InitiatorLoginStatistics, MSiSCSI_InitiatorLoginStatistics, *PMSiSCSI_InitiatorLoginStatistics
req.iface: 
---

# MSiSCSI_InitiatorLoginStatistics structure



## -description
<p>The MSiSCSI_InitiatorLoginStatistics structure is used by iSCSI initiators to report logon statistics. </p>


## -syntax

````
typedef struct _MSiSCSI_InitiatorLoginStatistics {
  ULONGLONG UniqueAdapterId;
  ULONG     LoginAcceptRsps;
  ULONG     LoginOtherFailRsps;
  ULONG     LoginRedirectRsps;
  ULONG     LoginAuthFailRsps;
  ULONG     LoginAuthenticateFails;
  ULONG     LoginNegotiateFails;
  ULONG     LogoutNormals;
  ULONG     LogoutOtherCodes;
  ULONG     LoginFailures;
} MSiSCSI_InitiatorLoginStatistics, *PMSiSCSI_InitiatorLoginStatistics;
````


## -struct-fields
<dl>

### -field <b>UniqueAdapterId</b>

<dd>
<p>A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID). The initiator reports this value in the <b>UniqueAdapterId</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563012">MSiSCSI_HBAInformation</a> structure.</p>
</dd>

### -field <b>LoginAcceptRsps</b>

<dd>
<p>The number of login accept responses. </p>
</dd>

### -field <b>LoginOtherFailRsps</b>

<dd>
<p>The number of failed responses.</p>
</dd>

### -field <b>LoginRedirectRsps</b>

<dd>
<p>The number of redirect responses.</p>
</dd>

### -field <b>LoginAuthFailRsps</b>

<dd>
<p>The number of logon responses that failed because the initiator and target did not have compatible authentication algorithms.</p>
</dd>

### -field <b>LoginAuthenticateFails</b>

<dd>
<p>The number of logons that failed because of a target authentication failure (the initiator and target did not have matching credentials).</p>
</dd>

### -field <b>LoginNegotiateFails</b>

<dd>
<p>The number of logons that failed because of negotiation failures.</p>
</dd>

### -field <b>LogoutNormals</b>

<dd>
<p>The number of logoff PDUs with a reason code of 0.</p>
</dd>

### -field <b>LogoutOtherCodes</b>

<dd>
<p>The number of logoff PDUs with a status code other than 0.</p>
</dd>

### -field <b>LoginFailures</b>

<dd>
<p>The number of times that a logon attempt by the initiator has failed.</p>
</dd>
</dl>

## -remarks
<p>It is optional that you implement this class.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsiprf.h (include Iscsiprf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563012">MSiSCSI_HBAInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563042">MSiSCSI_InitiatorLoginStatistics WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20MSiSCSI_InitiatorLoginStatistics structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
