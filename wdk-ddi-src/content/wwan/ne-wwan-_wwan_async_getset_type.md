---
UID: NE:wwan._WWAN_ASYNC_GETSET_TYPE
title: "_WWAN_ASYNC_GETSET_TYPE"
author: windows-driver-content
description: The WWAN_ASYNC_GETSET_TYPE enumeration lists the different asynchronous OID get/set requests.
old-location: netvista\wwan_async_getset_type.htm
old-project: netvista
ms.assetid: 2FECDA17-7B38-4636-AFAF-D923AECFAF68
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PWWAN_ASYNC_GETSET_TYPE, WWAN_ASYNC_GETSET_TYPE, WWAN_ASYNC_GETSET_TYPE enumeration [Network Drivers Starting with Windows Vista], WWAN_ASYNC_GETSET_TYPE_MAX, WwanAsyncAuthChallenge, WwanAsyncGetConnect, WwanAsyncGetDeviceCaps, WwanAsyncGetDeviceServiceCommand get request., WwanAsyncGetDeviceServices, WwanAsyncGetHomeProvider, WwanAsyncGetPacketService, WwanAsyncGetPin, WwanAsyncGetPinEx get request., WwanAsyncGetPinList, WwanAsyncGetPreferredProviders, WwanAsyncGetProvisionedContexts, WwanAsyncGetRadioState, WwanAsyncGetReadyInfo, WwanAsyncGetRegisterState, WwanAsyncGetSignalState, WwanAsyncGetSmsConfiguration, WwanAsyncGetVisibleProviders, WwanAsyncSetConnect, WwanAsyncSetDeviceServiceCommand, WwanAsyncSetHomeProvider, WwanAsyncSetPacketService, WwanAsyncSetPin, WwanAsyncSetPinEx, WwanAsyncSetPreferredProviders, WwanAsyncSetProfileIndex, WwanAsyncSetProvisionedContext, WwanAsyncSetRadioState, WwanAsyncSetRegisterState, WwanAsyncSetServiceActivation, WwanAsyncSetSignalState, WwanAsyncSetSmsConfiguration, WwanAsyncSetVendorSpecific, WwanAsyncSmsDelete, WwanAsyncSmsRead, WwanAsyncSmsSend, WwanAsyncSmsStatus, WwanAsyncSubscribeDeviceServiceEvents, WwanAsyncUssdRequest, _WWAN_ASYNC_GETSET_TYPE, netvista.wwan_async_getset_type, wwan/WWAN_ASYNC_GETSET_TYPE, wwan/WWAN_ASYNC_GETSET_TYPE_MAX, wwan/WwanAsyncAuthChallenge, wwan/WwanAsyncGetConnect, wwan/WwanAsyncGetDeviceCaps, wwan/WwanAsyncGetDeviceServiceCommand get request., wwan/WwanAsyncGetDeviceServices, wwan/WwanAsyncGetHomeProvider, wwan/WwanAsyncGetPacketService, wwan/WwanAsyncGetPin, wwan/WwanAsyncGetPinEx get request., wwan/WwanAsyncGetPinList, wwan/WwanAsyncGetPreferredProviders, wwan/WwanAsyncGetProvisionedContexts, wwan/WwanAsyncGetRadioState, wwan/WwanAsyncGetReadyInfo, wwan/WwanAsyncGetRegisterState, wwan/WwanAsyncGetSignalState, wwan/WwanAsyncGetSmsConfiguration, wwan/WwanAsyncGetVisibleProviders, wwan/WwanAsyncSetConnect, wwan/WwanAsyncSetDeviceServiceCommand, wwan/WwanAsyncSetHomeProvider, wwan/WwanAsyncSetPacketService, wwan/WwanAsyncSetPin, wwan/WwanAsyncSetPinEx, wwan/WwanAsyncSetPreferredProviders, wwan/WwanAsyncSetProfileIndex, wwan/WwanAsyncSetProvisionedContext, wwan/WwanAsyncSetRadioState, wwan/WwanAsyncSetRegisterState, wwan/WwanAsyncSetServiceActivation, wwan/WwanAsyncSetSignalState, wwan/WwanAsyncSetSmsConfiguration, wwan/WwanAsyncSetVendorSpecific, wwan/WwanAsyncSmsDelete, wwan/WwanAsyncSmsRead, wwan/WwanAsyncSmsSend, wwan/WwanAsyncSmsStatus, wwan/WwanAsyncSubscribeDeviceServiceEvents, wwan/WwanAsyncUssdRequest"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wwan.h
api_name:
-	WWAN_ASYNC_GETSET_TYPE
product: Windows
targetos: Windows
req.typenames: WWAN_ASYNC_GETSET_TYPE, *PWWAN_ASYNC_GETSET_TYPE
req.product: Windows 10 or later.
---

# _WWAN_ASYNC_GETSET_TYPE Enumeration
The WWAN_ASYNC_GETSET_TYPE enumeration lists the different asynchronous OID get/set requests.

## Syntax
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

## Constants

<table>
            
                <tr>
                    <td>WwanAsyncGetDeviceCaps</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569824">OID_WWAN_DEVICE_CAPS</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetReadyInfo</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569833">OID_WWAN_READY_INFO</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetRadioState</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569832">OID_WWAN_RADIO_STATE</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetRadioState</td>
                    <td>Asynchronous OID_WWAN_RADIO_STATE set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetPin</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569828">OID_WWAN_PIN</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetPin</td>
                    <td>Asynchronous OID_WWAN_PIN set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetPinList</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569829">OID_WWAN_PIN_LIST</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetHomeProvider</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569826">OID_WWAN_HOME_PROVIDER</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetHomeProvider</td>
                    <td>Asynchronous OID_WWAN_HOME_PROVIDER set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetPreferredProviders</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569830">OID_WWAN_PREFERRED_PROVIDERS</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetPreferredProviders</td>
                    <td>Asynchronous OID_WWAN_PREFERRED_PROVIDERS set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetVisibleProviders</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569843">OID_WWAN_VISIBLE_PROVIDERS</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetRegisterState</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569834">OID_WWAN_REGISTER_STATE</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetRegisterState</td>
                    <td>Asynchronous OID_WWAN_REGISTER_STATE set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetPacketService</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569827">OID_WWAN_PACKET_SERVICE</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetPacketService</td>
                    <td>Asynchronous OID_WWAN_PACKET_SERVICE set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetSignalState</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569836">OID_WWAN_SIGNAL_STATE</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetSignalState</td>
                    <td>Asynchronous OID_WWAN_SIGNAL_STATE set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetConnect</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569823">OID_WWAN_CONNECT</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetConnect</td>
                    <td>Asynchronous OID_WWAN_CONNECT set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetProvisionedContexts</td>
                    <td>Asynchronous <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-wwan-provisioned-contexts">OID_WWAN_PROVISIONED_CONTEXTS</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetProvisionedContext</td>
                    <td>Asynchronous OID_WWAN_PROVISIONED_CONTEXTS set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetServiceActivation</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569835">OID_WWAN_SERVICE_ACTIVATION</a> set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetSmsConfiguration</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569837">OID_WWAN_SMS_CONFIGURATION</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetSmsConfiguration</td>
                    <td>Asynchronous OID_WWAN_SMS_CONFIGURATION set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSmsRead</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569839">OID_WWAN_SMS_READ</a></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSmsSend</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569840">OID_WWAN_SMS_SEND</a></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSmsDelete</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569838">OID_WWAN_SMS_DELETE</a></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSmsStatus</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569841">OID_WWAN_SMS_STATUS</a></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetVendorSpecific</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/ff569842">OID_WWAN_VENDOR_SPECIFIC</a></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetProfileIndex</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetDeviceServices</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440093">OID_WWAN_DEVICE_SERVICES</a> get request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSubscribeDeviceServiceEvents</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440096">OID_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS</a></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncAuthChallenge</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440092">OID_WWAN_AUTH_CHALLENGE</a></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncUssdRequest</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440100">OID_WWAN_USSD</a></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetPinEx</td>
                    <td>Asynchronous <a href="https://msdn.microsoft.com/library/windows/hardware/hh440095">OID_WWAN_PIN_EX</a> set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetPinEx</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetDeviceServiceCommand</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetDeviceServiceCommand</td>
                    <td>Asynchronous OID_WWAN_DEVICE_SERVICE_COMMAND set request.</td>
                </tr>
            
                <tr>
                    <td>WwanAsyncQueryDeviceServiceSupportedCommands</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetPreferredMultiCarrierProviders</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetPreferredMultiCarrierProviders</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetDeviceServiceSession</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncWriteDeviceServiceSession</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetNetworkIdleHint</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetPreshutdown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetAtr</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncUiccOpenChannel</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncUiccCloseChannel</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncUiccSendApdu</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncUiccGetTerminalCapability</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncUiccSetTerminalCapability</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetPsMediaConfig</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetPsMediaConfig</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetSarConfig</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetSarConfig</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetSarTransmissionStatus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetSarTransmissionStatus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetNetworkBlacklist</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetNetworkBlacklist</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetLteAttachConfig</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetLteAttachConfig</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetLteAttachStatus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetLteAttachStatus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetProvisionedContextsV2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetProvisionedContextV2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetSysCap</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetDeviceCapsEx</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetUiccSlotMapping</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetUiccSlotMapping</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetUiccSlotInfo</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetModemConfigInfo</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetPcoStatus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncUiccGetReset</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncUiccSetReset</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncSetDeviceReset</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanAsyncGetCellInfo</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WWAN_ASYNC_GETSET_TYPE_MAX</td>
                    <td>The maximum number of entries in the WWAN_ASYNC_GETSET_TYPE enumeration.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with  Windows 8. Supported starting with  Windows 8. |
| **Header** | wwan.h |

## See Also

<a href="https://msdn.microsoft.com/922b6b55-c332-4721-bbd1-571b0e154df3">MB Data Model</a>