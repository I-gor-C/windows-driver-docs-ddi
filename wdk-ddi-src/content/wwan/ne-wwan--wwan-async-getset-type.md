---
UID: NE.wwan._WWAN_ASYNC_GETSET_TYPE
title: WWAN_ASYNC_GETSET_TYPE
author: windows-driver-content
description: The WWAN_ASYNC_GETSET_TYPE enumeration lists the different asynchronous OID get/set requests.
old-location: netvista\wwan_async_getset_type.htm
old-project: netvista
ms.assetid: 2FECDA17-7B38-4636-AFAF-D923AECFAF68
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_ASYNC_GETSET_TYPE
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
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_ASYNC_GETSET_TYPE enumeration



## -description
<p>The WWAN_ASYNC_GETSET_TYPE enumeration lists the different asynchronous OID get/set requests.</p>


## -syntax

````
typedef enum _WWAN_ASYNC_GETSET_TYPE { 
  WwanAsyncGetDeviceCaps                         = 0,
  WwanAsyncGetReadyInfo                          = ,
  WwanAsyncGetRadioState                         = ,
  WwanAsyncSetRadioState                         = ,
  WwanAsyncGetPin                                = ,
  WwanAsyncSetPin                                = ,
  WwanAsyncGetPinList                            = ,
  WwanAsyncGetHomeProvider                       = ,
  WwanAsyncSetHomeProvider                       = ,
  WwanAsyncGetPreferredProviders                 = ,
  WwanAsyncSetPreferredProviders                 = ,
  WwanAsyncGetVisibleProviders                   = ,
  WwanAsyncGetRegisterState                      = ,
  WwanAsyncSetRegisterState                      = ,
  WwanAsyncGetPacketService                      = ,
  WwanAsyncSetPacketService                      = ,
  WwanAsyncGetSignalState                        = ,
  WwanAsyncSetSignalState                        = ,
  WwanAsyncGetConnect                            = ,
  WwanAsyncSetConnect                            = ,
  WwanAsyncGetProvisionedContexts                = ,
  WwanAsyncSetProvisionedContext                 = ,
  WwanAsyncSetServiceActivation                  = ,
  WwanAsyncGetSmsConfiguration                   = ,
  WwanAsyncSetSmsConfiguration                   = ,
  WwanAsyncSmsRead                               = ,
  WwanAsyncSmsSend                               = ,
  WwanAsyncSmsDelete                             = ,
  WwanAsyncSmsStatus                             = ,
  WwanAsyncSetVendorSpecific                     = ,
  WwanAsyncSetProfileIndex                       = ,
  WwanAsyncGetDeviceServices                     = ,
  WwanAsyncSubscribeDeviceServiceEvents          = ,
  WwanAsyncAuthChallenge                         = ,
  WwanAsyncUssdRequest                           = ,
  WwanAsyncSetPinEx                              = ,
  WwanAsyncGetPinEx get request.                 = ,
  WwanAsyncGetDeviceServiceCommand get request.  = ,
  WwanAsyncSetDeviceServiceCommand               = ,
  WWAN_ASYNC_GETSET_TYPE_MAX                     = 
} WWAN_ASYNC_GETSET_TYPE;
````


## -enum-fields
<dl>

### -field WwanAsyncGetDeviceCaps

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569824">OID_WWAN_DEVICE_CAPS</a> get request.</p>
</dd>

### -field WwanAsyncGetReadyInfo

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569833">OID_WWAN_READY_INFO</a> get request.</p>
</dd>

### -field WwanAsyncGetRadioState

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569832">OID_WWAN_RADIO_STATE</a> get request.</p>
</dd>

### -field WwanAsyncSetRadioState

<dd>
<p>Asynchronous OID_WWAN_RADIO_STATE set request.</p>
</dd>

### -field WwanAsyncGetPin

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569828">OID_WWAN_PIN</a> get request.</p>
</dd>

### -field WwanAsyncSetPin

<dd>
<p>Asynchronous OID_WWAN_PIN set request.</p>
</dd>

### -field WwanAsyncGetPinList

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569829">OID_WWAN_PIN_LIST</a> get request.</p>
</dd>

### -field WwanAsyncGetHomeProvider

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569826">OID_WWAN_HOME_PROVIDER</a> get request.</p>
</dd>

### -field WwanAsyncSetHomeProvider

<dd>
<p>Asynchronous OID_WWAN_HOME_PROVIDER set request.</p>
</dd>

### -field WwanAsyncGetPreferredProviders

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569830">OID_WWAN_PREFERRED_PROVIDERS</a> get request.</p>
</dd>

### -field WwanAsyncSetPreferredProviders

<dd>
<p>Asynchronous OID_WWAN_PREFERRED_PROVIDERS set request.</p>
</dd>

### -field WwanAsyncGetVisibleProviders

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569843">OID_WWAN_VISIBLE_PROVIDERS</a> get request.</p>
</dd>

### -field WwanAsyncGetRegisterState

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569834">OID_WWAN_REGISTER_STATE</a> get request.</p>
</dd>

### -field WwanAsyncSetRegisterState

<dd>
<p>Asynchronous OID_WWAN_REGISTER_STATE set request.</p>
</dd>

### -field WwanAsyncGetPacketService

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569827">OID_WWAN_PACKET_SERVICE</a> get request.</p>
</dd>

### -field WwanAsyncSetPacketService

<dd>
<p>Asynchronous OID_WWAN_PACKET_SERVICE set request.</p>
</dd>

### -field WwanAsyncGetSignalState

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569836">OID_WWAN_SIGNAL_STATE</a> get request.</p>
</dd>

### -field WwanAsyncSetSignalState

<dd>
<p>Asynchronous OID_WWAN_SIGNAL_STATE set request.</p>
</dd>

### -field WwanAsyncGetConnect

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569823">OID_WWAN_CONNECT</a> get request.</p>
</dd>

### -field WwanAsyncSetConnect

<dd>
<p>Asynchronous OID_WWAN_CONNECT set request.</p>
</dd>

### -field WwanAsyncGetProvisionedContexts

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569831">OID_WWAN_PROVISIONED_CONTEXTS</a> get request.</p>
</dd>

### -field WwanAsyncSetProvisionedContext

<dd>
<p>Asynchronous OID_WWAN_PROVISIONED_CONTEXTS set request.</p>
</dd>

### -field WwanAsyncSetServiceActivation

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569835">OID_WWAN_SERVICE_ACTIVATION</a> set request.</p>
</dd>

### -field WwanAsyncGetSmsConfiguration

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569837">OID_WWAN_SMS_CONFIGURATION</a> get request.</p>
</dd>

### -field WwanAsyncSetSmsConfiguration

<dd>
<p>Asynchronous OID_WWAN_SMS_CONFIGURATION set request.</p>
</dd>

### -field WwanAsyncSmsRead

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569839">OID_WWAN_SMS_READ</a>
</p>
</dd>

### -field WwanAsyncSmsSend

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569840">OID_WWAN_SMS_SEND</a>
</p>
</dd>

### -field WwanAsyncSmsDelete

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569838">OID_WWAN_SMS_DELETE</a>
</p>
</dd>

### -field WwanAsyncSmsStatus

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569841">OID_WWAN_SMS_STATUS</a>
</p>
</dd>

### -field WwanAsyncSetVendorSpecific

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569842">OID_WWAN_VENDOR_SPECIFIC</a>
</p>
</dd>

### -field WwanAsyncSetProfileIndex

<dd>
<p>Reserved.</p>
</dd>

### -field WwanAsyncGetDeviceServices

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440093">OID_WWAN_DEVICE_SERVICES</a> get request.</p>
</dd>

### -field WwanAsyncSubscribeDeviceServiceEvents

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440096">OID_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS</a>
</p>
</dd>

### -field WwanAsyncAuthChallenge

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440092">OID_WWAN_AUTH_CHALLENGE</a>
</p>
</dd>

### -field WwanAsyncUssdRequest

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440100">OID_WWAN_USSD</a>
</p>
</dd>

### -field WwanAsyncSetPinEx

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440095">OID_WWAN_PIN_EX</a> set request.</p>
</dd>

### -field WwanAsyncGetPinEx get request.

<dd>
<p>Asynchronous OID_WWAN_PIN_EX get request.</p>
</dd>

### -field WwanAsyncGetDeviceServiceCommand get request.

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440094">OID_WWAN_DEVICE_SERVICE_COMMAND</a>
</p>
</dd>

### -field WwanAsyncSetDeviceServiceCommand

<dd>
<p>Asynchronous OID_WWAN_DEVICE_SERVICE_COMMAND set request.</p>
</dd>

### -field WWAN_ASYNC_GETSET_TYPE_MAX

<dd>
<p>The maximum number of entries in the WWAN_ASYNC_GETSET_TYPE enumeration.</p>
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
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.mb_data_model">MB Data Model</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_ASYNC_GETSET_TYPE enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
