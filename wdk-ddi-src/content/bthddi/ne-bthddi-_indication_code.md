---
UID: NE:bthddi._INDICATION_CODE
title: "_INDICATION_CODE"
author: windows-driver-content
description: The INDICATION_CODE enumeration type indicates to a profile driver what type of L2CAP event has occurred.
old-location: bltooth\indication_code.htm
old-project: bltooth
ms.assetid: 7fc374e3-ca5b-476d-bc44-afb28ecf9920
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PINDICATION_CODE, INDICATION_CODE, INDICATION_CODE enumeration [Bluetooth Devices], IndicationAddReference, IndicationFreeExtraOptions, IndicationPairDevice, IndicationRecvPacket, IndicationReleaseReference, IndicationRemoteConfigRequest, IndicationRemoteConfigResponse, IndicationRemoteConnect, IndicationRemoteConnectLE, IndicationRemoteDisconnect, IndicationUnpairDevice, IndicationUnpersonalizeDevice, PINDICATION_CODE, PINDICATION_CODE enumeration pointer [Bluetooth Devices], _INDICATION_CODE, bltooth.indication_code, bth_enums_89c3fcea-8183-4227-b3fb-4e18c3612326.xml, bthddi/INDICATION_CODE, bthddi/IndicationAddReference, bthddi/IndicationFreeExtraOptions, bthddi/IndicationPairDevice, bthddi/IndicationRecvPacket, bthddi/IndicationReleaseReference, bthddi/IndicationRemoteConfigRequest, bthddi/IndicationRemoteConfigResponse, bthddi/IndicationRemoteConnect, bthddi/IndicationRemoteConnectLE, bthddi/IndicationRemoteDisconnect, bthddi/IndicationUnpairDevice, bthddi/IndicationUnpersonalizeDevice, bthddi/PINDICATION_CODE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions:\_Supported in Windows Vista, and later.
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
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	bthddi.h
api_name:
-	INDICATION_CODE
product:
- Windows
targetos: Windows
req.typenames: INDICATION_CODE, *PINDICATION_CODE, INDICATION_CODE, *PINDICATION_CODE
---

# _INDICATION_CODE Enumeration
The INDICATION_CODE enumeration type indicates to a profile driver what type of L2CAP event has
  occurred.

## Syntax
```
typedef enum _INDICATION_CODE {
  IndicationAddReference          ,
  IndicationReleaseReference      ,
  IndicationRemoteConnect         ,
  IndicationRemoteDisconnect      ,
  IndicationRemoteConfigRequest   ,
  IndicationRemoteConfigResponse  ,
  IndicationFreeExtraOptions      ,
  IndicationRecvPacket            ,
  IndicationPairDevice            ,
  IndicationUnpairDevice          ,
  IndicationUnpersonalizeDevice   ,
  IndicationRemoteConnectLE
} *PINDICATION_CODE, INDICATION_CODE;
```

## Constants

<table>
            
                <tr>
                    <td>IndicationAddReference</td>
                    <td>Indicates to a profile driver to add a reference to its device object because it may be called at
     any time.</td>
                </tr>
            
                <tr>
                    <td>IndicationReleaseReference</td>
                    <td>Indicates to a profile driver to release a reference to its device object and that it will no
     longer be called.</td>
                </tr>
            
                <tr>
                    <td>IndicationRemoteConnect</td>
                    <td>Indicates to a server profile driver that a remote device is connecting to the PSM that the
     profile driver registered earlier. Profile drivers accept or reject this request by 
     <a href="https://msdn.microsoft.com/53a692e7-9c71-4dca-9331-32ac97b94179">building and sending</a> a 
     <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff536616">
     BRB_L2CA_OPEN_CHANNEL_RESPONSE</a> request. When this indication code is passed, the profile driver
     should use the parameters that are passed to it in the 
     <b>Connect</b> member of the 
     <a href="https://msdn.microsoft.com/fc93ab8a-01d2-4827-8d89-06f09bf10456">
     INDICATION_PARAMETERS</a> structure.</td>
                </tr>
            
                <tr>
                    <td>IndicationRemoteDisconnect</td>
                    <td>Indicates to a registered profile driver that a remote device disconnecting from the local radio.
     When this indication code is passed, the profile driver should use the parameters that are passed to it
     in the 
     <b>Disconnect</b> member of the INDICATION_PARAMETERS structure.</td>
                </tr>
            
                <tr>
                    <td>IndicationRemoteConfigRequest</td>
                    <td>Indicates to a client profile driver that a remote device is performing a configuration request.
     When this indication code is passed, the profile driver should use the parameters that are passed to it
     in the 
     <b>ConfigRequest</b> member of the INDICATION_PARAMETERS structure.</td>
                </tr>
            
                <tr>
                    <td>IndicationRemoteConfigResponse</td>
                    <td>Indicates to a client profile driver that a remote device is responding to a configuration
     request. When this indication code is passed, the profile driver should use the parameters that are
     passed to it in the 
     <b>ConfigResponse</b> member of the INDICATION_PARAMETERS structure.</td>
                </tr>
            
                <tr>
                    <td>IndicationFreeExtraOptions</td>
                    <td>Reserved for future use. Do not use.</td>
                </tr>
            
                <tr>
                    <td>IndicationRecvPacket</td>
                    <td>Indicates to a registered profile driver that a packet has been received on the specified PSM. The
     profile driver can use this event to determine when it is necessary to issue a read
     BRB_L2CA_ACL_TRANSFTER BRB. Profile drivers that need to read from the remote device can also ignore
     this notification and keep a read BRB pending at all times. When this indication code is passed, the
     profile driver should use the parameters that are passed to it in the 
     <b>RecvPacket</b> member of the 
     <a href="https://msdn.microsoft.com/fc93ab8a-01d2-4827-8d89-06f09bf10456">
     INDICATION_PARAMETERS</a> structure.</td>
                </tr>
            
                <tr>
                    <td>IndicationPairDevice</td>
                    <td>Indicates to a registered driver that the local radio has bonded to a specific remote
     radio.</td>
                </tr>
            
                <tr>
                    <td>IndicationUnpairDevice</td>
                    <td>Indicates to a registered driver that the local radio is no longer bonded to a specific remote
     radio.</td>
                </tr>
            
                <tr>
                    <td>IndicationUnpersonalizeDevice</td>
                    <td>Indicates to a registered driver that the specified remote radio has been removed from the list of
     personal devices.</td>
                </tr>
            
                <tr>
                    <td>IndicationRemoteConnectLE</td>
                    <td>Indicates to a server profile driver that a low energy (LE) remote device is connecting to the PSM that the
     profile driver registered earlier. Profile drivers accept or reject this request by 
     <a href="https://msdn.microsoft.com/53a692e7-9c71-4dca-9331-32ac97b94179">building and sending</a> a 
     <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff536616">
     BRB_L2CA_OPEN_CHANNEL_RESPONSE</a> request. When this indication code is passed, the profile driver
     should use the parameters that are passed to it in the 
     <b>Connect</b> member of the 
     <a href="https://msdn.microsoft.com/fc93ab8a-01d2-4827-8d89-06f09bf10456">
     INDICATION_PARAMETERS</a> structure. This value is present in Windows 8 and later versions of Windows.</td>
                </tr>
</table>

## Remarks

A value from this enumeration is passed to a profile driver's 
    <a href="https://msdn.microsoft.com/d3ca900d-1dd6-49da-ae94-855de3fbd086">L2CAP Callback Function</a> to notify
    it of an event.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Versions:\_Supported in Windows Vista, and later. Versions:\_Supported in Windows Vista, and later. |
| **Header** | bthddi.h (include Bthddi.h) |

## See Also

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff536618">BRB_L2CA_REGISTER_SERVER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536680">INDICATION_PARAMETERS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536751">IOCTL_INTERNAL_BTH_SUBMIT_BRB</a>



<a href="https://msdn.microsoft.com/d3ca900d-1dd6-49da-ae94-855de3fbd086">L2CAP Callback Function</a>