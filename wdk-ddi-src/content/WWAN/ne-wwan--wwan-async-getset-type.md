---
UID: NE.wwan._WWAN_ASYNC_GETSET_TYPE
title: WWAN_ASYNC_GETSET_TYPE
author: windows-driver-content
description: The WWAN_ASYNC_GETSET_TYPE enumeration lists the different asynchronous OID get/set requests.
old-location: netvista\wwan_async_getset_type.htm
ms.assetid: 2FECDA17-7B38-4636-AFAF-D923AECFAF68
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
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

### -field <a id="WwanAsyncGetDeviceCaps"></a><a id="wwanasyncgetdevicecaps"></a><a id="WWANASYNCGETDEVICECAPS"></a><b>WwanAsyncGetDeviceCaps</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569824">OID_WWAN_DEVICE_CAPS</a> get request.</p>
</dd>

### -field <a id="WwanAsyncGetReadyInfo"></a><a id="wwanasyncgetreadyinfo"></a><a id="WWANASYNCGETREADYINFO"></a><b>WwanAsyncGetReadyInfo</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569833">OID_WWAN_READY_INFO</a> get request.</p>
</dd>

### -field <a id="WwanAsyncGetRadioState"></a><a id="wwanasyncgetradiostate"></a><a id="WWANASYNCGETRADIOSTATE"></a><b>WwanAsyncGetRadioState</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569832">OID_WWAN_RADIO_STATE</a> get request.</p>
</dd>

### -field <a id="WwanAsyncSetRadioState"></a><a id="wwanasyncsetradiostate"></a><a id="WWANASYNCSETRADIOSTATE"></a><b>WwanAsyncSetRadioState</b>

<dd>
<p>Asynchronous OID_WWAN_RADIO_STATE set request.</p>
</dd>

### -field <a id="WwanAsyncGetPin"></a><a id="wwanasyncgetpin"></a><a id="WWANASYNCGETPIN"></a><b>WwanAsyncGetPin</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569828">OID_WWAN_PIN</a> get request.</p>
</dd>

### -field <a id="WwanAsyncSetPin"></a><a id="wwanasyncsetpin"></a><a id="WWANASYNCSETPIN"></a><b>WwanAsyncSetPin</b>

<dd>
<p>Asynchronous OID_WWAN_PIN set request.</p>
</dd>

### -field <a id="WwanAsyncGetPinList"></a><a id="wwanasyncgetpinlist"></a><a id="WWANASYNCGETPINLIST"></a><b>WwanAsyncGetPinList</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569829">OID_WWAN_PIN_LIST</a> get request.</p>
</dd>

### -field <a id="WwanAsyncGetHomeProvider"></a><a id="wwanasyncgethomeprovider"></a><a id="WWANASYNCGETHOMEPROVIDER"></a><b>WwanAsyncGetHomeProvider</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569826">OID_WWAN_HOME_PROVIDER</a> get request.</p>
</dd>

### -field <a id="WwanAsyncSetHomeProvider"></a><a id="wwanasyncsethomeprovider"></a><a id="WWANASYNCSETHOMEPROVIDER"></a><b>WwanAsyncSetHomeProvider</b>

<dd>
<p>Asynchronous OID_WWAN_HOME_PROVIDER set request.</p>
</dd>

### -field <a id="WwanAsyncGetPreferredProviders"></a><a id="wwanasyncgetpreferredproviders"></a><a id="WWANASYNCGETPREFERREDPROVIDERS"></a><b>WwanAsyncGetPreferredProviders</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569830">OID_WWAN_PREFERRED_PROVIDERS</a> get request.</p>
</dd>

### -field <a id="WwanAsyncSetPreferredProviders"></a><a id="wwanasyncsetpreferredproviders"></a><a id="WWANASYNCSETPREFERREDPROVIDERS"></a><b>WwanAsyncSetPreferredProviders</b>

<dd>
<p>Asynchronous OID_WWAN_PREFERRED_PROVIDERS set request.</p>
</dd>

### -field <a id="WwanAsyncGetVisibleProviders"></a><a id="wwanasyncgetvisibleproviders"></a><a id="WWANASYNCGETVISIBLEPROVIDERS"></a><b>WwanAsyncGetVisibleProviders</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569843">OID_WWAN_VISIBLE_PROVIDERS</a> get request.</p>
</dd>

### -field <a id="WwanAsyncGetRegisterState"></a><a id="wwanasyncgetregisterstate"></a><a id="WWANASYNCGETREGISTERSTATE"></a><b>WwanAsyncGetRegisterState</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569834">OID_WWAN_REGISTER_STATE</a> get request.</p>
</dd>

### -field <a id="WwanAsyncSetRegisterState"></a><a id="wwanasyncsetregisterstate"></a><a id="WWANASYNCSETREGISTERSTATE"></a><b>WwanAsyncSetRegisterState</b>

<dd>
<p>Asynchronous OID_WWAN_REGISTER_STATE set request.</p>
</dd>

### -field <a id="WwanAsyncGetPacketService"></a><a id="wwanasyncgetpacketservice"></a><a id="WWANASYNCGETPACKETSERVICE"></a><b>WwanAsyncGetPacketService</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569827">OID_WWAN_PACKET_SERVICE</a> get request.</p>
</dd>

### -field <a id="WwanAsyncSetPacketService"></a><a id="wwanasyncsetpacketservice"></a><a id="WWANASYNCSETPACKETSERVICE"></a><b>WwanAsyncSetPacketService</b>

<dd>
<p>Asynchronous OID_WWAN_PACKET_SERVICE set request.</p>
</dd>

### -field <a id="WwanAsyncGetSignalState"></a><a id="wwanasyncgetsignalstate"></a><a id="WWANASYNCGETSIGNALSTATE"></a><b>WwanAsyncGetSignalState</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569836">OID_WWAN_SIGNAL_STATE</a> get request.</p>
</dd>

### -field <a id="WwanAsyncSetSignalState"></a><a id="wwanasyncsetsignalstate"></a><a id="WWANASYNCSETSIGNALSTATE"></a><b>WwanAsyncSetSignalState</b>

<dd>
<p>Asynchronous OID_WWAN_SIGNAL_STATE set request.</p>
</dd>

### -field <a id="WwanAsyncGetConnect"></a><a id="wwanasyncgetconnect"></a><a id="WWANASYNCGETCONNECT"></a><b>WwanAsyncGetConnect</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569823">OID_WWAN_CONNECT</a> get request.</p>
</dd>

### -field <a id="WwanAsyncSetConnect"></a><a id="wwanasyncsetconnect"></a><a id="WWANASYNCSETCONNECT"></a><b>WwanAsyncSetConnect</b>

<dd>
<p>Asynchronous OID_WWAN_CONNECT set request.</p>
</dd>

### -field <a id="WwanAsyncGetProvisionedContexts"></a><a id="wwanasyncgetprovisionedcontexts"></a><a id="WWANASYNCGETPROVISIONEDCONTEXTS"></a><b>WwanAsyncGetProvisionedContexts</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569831">OID_WWAN_PROVISIONED_CONTEXTS</a> get request.</p>
</dd>

### -field <a id="WwanAsyncSetProvisionedContext"></a><a id="wwanasyncsetprovisionedcontext"></a><a id="WWANASYNCSETPROVISIONEDCONTEXT"></a><b>WwanAsyncSetProvisionedContext</b>

<dd>
<p>Asynchronous OID_WWAN_PROVISIONED_CONTEXTS set request.</p>
</dd>

### -field <a id="WwanAsyncSetServiceActivation"></a><a id="wwanasyncsetserviceactivation"></a><a id="WWANASYNCSETSERVICEACTIVATION"></a><b>WwanAsyncSetServiceActivation</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569835">OID_WWAN_SERVICE_ACTIVATION</a> set request.</p>
</dd>

### -field <a id="WwanAsyncGetSmsConfiguration"></a><a id="wwanasyncgetsmsconfiguration"></a><a id="WWANASYNCGETSMSCONFIGURATION"></a><b>WwanAsyncGetSmsConfiguration</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569837">OID_WWAN_SMS_CONFIGURATION</a> get request.</p>
</dd>

### -field <a id="WwanAsyncSetSmsConfiguration"></a><a id="wwanasyncsetsmsconfiguration"></a><a id="WWANASYNCSETSMSCONFIGURATION"></a><b>WwanAsyncSetSmsConfiguration</b>

<dd>
<p>Asynchronous OID_WWAN_SMS_CONFIGURATION set request.</p>
</dd>

### -field <a id="WwanAsyncSmsRead"></a><a id="wwanasyncsmsread"></a><a id="WWANASYNCSMSREAD"></a><b>WwanAsyncSmsRead</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569839">OID_WWAN_SMS_READ</a>
</p>
</dd>

### -field <a id="WwanAsyncSmsSend"></a><a id="wwanasyncsmssend"></a><a id="WWANASYNCSMSSEND"></a><b>WwanAsyncSmsSend</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569840">OID_WWAN_SMS_SEND</a>
</p>
</dd>

### -field <a id="WwanAsyncSmsDelete"></a><a id="wwanasyncsmsdelete"></a><a id="WWANASYNCSMSDELETE"></a><b>WwanAsyncSmsDelete</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569838">OID_WWAN_SMS_DELETE</a>
</p>
</dd>

### -field <a id="WwanAsyncSmsStatus"></a><a id="wwanasyncsmsstatus"></a><a id="WWANASYNCSMSSTATUS"></a><b>WwanAsyncSmsStatus</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569841">OID_WWAN_SMS_STATUS</a>
</p>
</dd>

### -field <a id="WwanAsyncSetVendorSpecific"></a><a id="wwanasyncsetvendorspecific"></a><a id="WWANASYNCSETVENDORSPECIFIC"></a><b>WwanAsyncSetVendorSpecific</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569842">OID_WWAN_VENDOR_SPECIFIC</a>
</p>
</dd>

### -field <a id="WwanAsyncSetProfileIndex"></a><a id="wwanasyncsetprofileindex"></a><a id="WWANASYNCSETPROFILEINDEX"></a><b>WwanAsyncSetProfileIndex</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <a id="WwanAsyncGetDeviceServices"></a><a id="wwanasyncgetdeviceservices"></a><a id="WWANASYNCGETDEVICESERVICES"></a><b>WwanAsyncGetDeviceServices</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440093">OID_WWAN_DEVICE_SERVICES</a> get request.</p>
</dd>

### -field <a id="WwanAsyncSubscribeDeviceServiceEvents"></a><a id="wwanasyncsubscribedeviceserviceevents"></a><a id="WWANASYNCSUBSCRIBEDEVICESERVICEEVENTS"></a><b>WwanAsyncSubscribeDeviceServiceEvents</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440096">OID_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS</a>
</p>
</dd>

### -field <a id="WwanAsyncAuthChallenge"></a><a id="wwanasyncauthchallenge"></a><a id="WWANASYNCAUTHCHALLENGE"></a><b>WwanAsyncAuthChallenge</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440092">OID_WWAN_AUTH_CHALLENGE</a>
</p>
</dd>

### -field <a id="WwanAsyncUssdRequest"></a><a id="wwanasyncussdrequest"></a><a id="WWANASYNCUSSDREQUEST"></a><b>WwanAsyncUssdRequest</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440100">OID_WWAN_USSD</a>
</p>
</dd>

### -field <a id="WwanAsyncSetPinEx"></a><a id="wwanasyncsetpinex"></a><a id="WWANASYNCSETPINEX"></a><b>WwanAsyncSetPinEx</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440095">OID_WWAN_PIN_EX</a> set request.</p>
</dd>

### -field <a id="WwanAsyncGetPinEx_get_request."></a><a id="wwanasyncgetpinex_get_request."></a><a id="WWANASYNCGETPINEX_GET_REQUEST."></a><b>WwanAsyncGetPinEx get request.</b>

<dd>
<p>Asynchronous OID_WWAN_PIN_EX get request.</p>
</dd>

### -field <a id="WwanAsyncGetDeviceServiceCommand_get_request."></a><a id="wwanasyncgetdeviceservicecommand_get_request."></a><a id="WWANASYNCGETDEVICESERVICECOMMAND_GET_REQUEST."></a><b>WwanAsyncGetDeviceServiceCommand get request.</b>

<dd>
<p>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440094">OID_WWAN_DEVICE_SERVICE_COMMAND</a>
</p>
</dd>

### -field <a id="WwanAsyncSetDeviceServiceCommand"></a><a id="wwanasyncsetdeviceservicecommand"></a><a id="WWANASYNCSETDEVICESERVICECOMMAND"></a><b>WwanAsyncSetDeviceServiceCommand</b>

<dd>
<p>Asynchronous OID_WWAN_DEVICE_SERVICE_COMMAND set request.</p>
</dd>

### -field <a id="WWAN_ASYNC_GETSET_TYPE_MAX"></a><a id="wwan_async_getset_type_max"></a><b>WWAN_ASYNC_GETSET_TYPE_MAX</b>

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
<a href="NULL">MB Data Model</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_ASYNC_GETSET_TYPE enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
