---
UID: NS.NDISWWAN._NDIS_WWAN_SMS_CONFIGURATION
title: _NDIS_WWAN_SMS_CONFIGURATION
author: windows-driver-content
description: The NDIS_WWAN_SMS_CONFIGURATION structure represents the SMS configuration of the MB device.
old-location: netvista\ndis_wwan_sms_configuration.htm
old-project: netvista
ms.assetid: 77d62078-7421-40c7-b743-fbc09b0eb5f9
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _NDIS_WWAN_SMS_CONFIGURATION, NDIS_WWAN_SMS_CONFIGURATION, *PNDIS_WWAN_SMS_CONFIGURATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_SMS_CONFIGURATION
req.alt-loc: ndiswwan.h
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
---

# _NDIS_WWAN_SMS_CONFIGURATION structure



## -description
The NDIS_WWAN_SMS_CONFIGURATION structure represents the SMS configuration of the MB device.


## -syntax

````
typedef struct _NDIS_WWAN_SMS_CONFIGURATION {
  NDIS_OBJECT_HEADER     Header;
  WWAN_STATUS            uStatus;
  WWAN_SMS_CONFIGURATION SmsConfiguration;
} NDIS_WWAN_SMS_CONFIGURATION, *PNDIS_WWAN_SMS_CONFIGURATION;
````


## -struct-fields

### -field Header

The header with type, revision, and size information about the NDIS_WWAN_SMS_CONFIGURATION
     structure. When the MB Service
     sends the data structure to the miniport driver for 
     <i>set</i> operations, it sets the header with the values that are shown in the following table. Miniport drivers must set the header with the same values when they send the data
     structure to the MB service.
     
<table>
<tr>
<th>Header submember</th>
<th>Value</th>
</tr>
<tr>
<td>
Type
</td>
<td>
NDIS_OBJECT_TYPE_DEFAULT
</td>
</tr>
<tr>
<td>
Revision
</td>
<td>
NDIS_WWAN_SMS_CONFIGURATION_REVISION_1
</td>
</tr>
<tr>
<td>
Size
</td>
<td>
sizeof(NDIS_WWAN_SMS_CONFIGURATION)
</td>
</tr>
</table>
 
For more information about these members, see 
     <a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a>.

### -field uStatus

The status of the SMS configuration operation. The following table shows the possible values for
     this member.
     
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
WWAN_STATUS_NOT_INITIALIZED
</td>
<td>
The operation failed because the device is in the process of initializing. Retry the operation
        after the ready-state of the device changes to 
        <b>WwanReadyStateInitialized</b>.
</td>
</tr>
<tr>
<td>
WWAN_STATUS_PIN_REQUIRED
</td>
<td>
The operation failed because the device requires a PIN.
</td>
</tr>
<tr>
<td>
WWAN_STATUS_SIM_NOT_INSERTED
</td>
<td>
The operation failed because the SIM card was not inserted fully into the device.
</td>
</tr>
<tr>
<td>
WWAN_STATUS_BAD_SIM
</td>
<td>
The operation failed because a faulty SIM card was detected.
</td>
</tr>
<tr>
<td>
WWAN_STATUS_SMS_UNKNOWN_ERROR
</td>
<td>
The operation failed because of an unknown error.
</td>
</tr>
<tr>
<td>
WWAN_STATUS_SMS_FORMAT_NOT_SUPPORTED
</td>
<td>
The operation failed because the SMS format specified in <a href="netvista.wwan_sms_configuration">WWAN_SMS_CONFIGURATION</a> is not supported.
</td>
</tr>
</table>
 

### -field SmsConfiguration

A formatted 
     <a href="netvista.wwan_sms_configuration">WWAN_SMS_CONFIGURATION</a> object that
     represents the SMS configuration of the MB device.

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
<dt>Ndiswwan.h (include Ndiswwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.wwan_sms_configuration">WWAN_SMS_CONFIGURATION</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_SMS_CONFIGURATION structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
