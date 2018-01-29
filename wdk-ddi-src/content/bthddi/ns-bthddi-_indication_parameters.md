---
UID : NS:bthddi._INDICATION_PARAMETERS
title : _INDICATION_PARAMETERS
author : windows-driver-content
description : The INDICATION_PARAMETERS structure is passed as the Parameters parameter to a profile driver's L2CAP Callback Function.
old-location : bltooth\indication_parameters.htm
old-project : bltooth
ms.assetid : fc93ab8a-01d2-4827-8d89-06f09bf10456
ms.author : windowsdriverdev
ms.date : 12/21/2017
ms.keywords : INDICATION_PARAMETERS, PINDICATION_PARAMETERS structure pointer [Bluetooth Devices], bltooth.indication_parameters, bthddi/INDICATION_PARAMETERS, *PINDICATION_PARAMETERS, bthddi/PINDICATION_PARAMETERS, PINDICATION_PARAMETERS, bth_structs_8cf076cf-a280-49ee-bbe6-cc54e854905e.xml, INDICATION_PARAMETERS structure [Bluetooth Devices], _INDICATION_PARAMETERS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : bthddi.h
req.include-header : Bthddi.h
req.target-type : Windows
req.target-min-winverclnt : Versions: Supported in Windows Vista, and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : INDICATION_PARAMETERS, *PINDICATION_PARAMETERS
---

# _INDICATION_PARAMETERS structure
The INDICATION_PARAMETERS structure is passed as the 
  <i>Parameters</i> parameter to a profile driver's 
  <a href="..\bthddi\nc-bthddi-pfnbthport_indication_callback.md">L2CAP Callback Function</a>.

## Syntax
````
typedef struct _INDICATION_PARAMETERS {
  L2CAP_CHANNEL_HANDLE ConnectionHandle;
  BTH_ADDR             BtAddress;
  union {
    struct {
      struct {
        USHORT PSM;
      } Request;
    } Connect;
    struct {
      CHANNEL_CONFIG_PARAMETERS CurrentParams;
      CHANNEL_CONFIG_PARAMETERS RequestedParams;
      CHANNEL_CONFIG_PARAMETERS ResponseParams;
      USHORT                    Response;
    } ConfigRequest;
    struct {
      CHANNEL_CONFIG_PARAMETERS CurrentParams;
      CHANNEL_CONFIG_PARAMETERS RequestedParams;
      CHANNEL_CONFIG_PARAMETERS RejectedParams;
      PCO_TYPE                  UnknownTypes;
      ULONG                     NumUnknownTypes;
      CHANNEL_CONFIG_PARAMETERS NewRequestParams;
      USHORT                    Response;
    } ConfigResponse;
    struct {
      ULONG                NumExtraOptions;
      PL2CAP_CONFIG_OPTION ExtraOptions;
    } FreeExtraOptions;
    struct {
      L2CAP_DISCONNECT_REASON Reason;
      BOOLEAN                 CloseNow;
    } Disconnect;
    struct {
      ULONG PacketLength;
      ULONG TotalQueueLength;
    } RecvPacket;
  } Parameters;
} INDICATION_PARAMETERS, *PINDICATION_PARAMETERS;
````

## Members


`BtAddress`

The Bluetooth address of the remote device.

`ConnectionHandle`

The L2CAP connection handle to the remote device. This handle is only valid for notifications that
     arrive over an established L2CAP connection.

`Parameters`



## Remarks
A profile driver's 
    <a href="..\bthddi\nc-bthddi-pfnbthport_indication_callback.md">L2CAP Callback Function</a> should
    process this structure differently depending upon the value that the Bluetooth driver stack passes in the
    
    <i>Indication</i> parameter of the callback function.

When the Bluetooth driver stack passes 
    <b>IndicationRemoteConnect</b>, the callback function should use the 
    <b>Connect</b> member of the 
    <b>Parameters</b> union.

When the Bluetooth driver stack passes 
    <b>IndicationRemoteDisconnect</b>, the callback function should use the 
    <b>Disconnect</b> member of the 
    <b>Parameters</b> union.

When the Bluetooth driver stack passes 
    <b>IndicationRemoteConfigRequest</b>, the callback function should use the 
    <b>ConfigRequest</b> member of the 
    <b>Parameters</b> union.

When the Bluetooth driver stack passes 
    <b>IndicationRemoteConfigResponse</b>, the callback function should use the 
    <b>ConfigResponse</b> member of the 
    <b>Parameters</b> union.

When the Bluetooth driver stack passes 
    <b>IndicationRemoteFreeExtraOptions</b>, the callback function should use the 
    <b>FreeExtraOptions</b> member of the 
    <b>Parameters</b> union.

When the Bluetooth driver stack passes 
    <b>IndicationRemoteRecvPacket</b>, the callback function should use the 
    <b>RecvPacket</b> member of the 
    <b>Parameters</b> union.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | bthddi.h (include Bthddi.h) |

## See Also

<a href="..\bthddi\ns-bthddi-_l2cap_config_option.md">L2CAP_CONFIG_OPTION</a>

<a href="..\bthddi\nc-bthddi-pfnbthport_indication_callback.md">L2CAP Callback Function</a>

<a href="..\bthddi\ne-bthddi-_l2cap_disconnect_reason.md">L2CAP_DISCONNECT_REASON</a>

<a href="..\bthddi\ns-bthddi-_channel_config_parameters.md">CHANNEL_CONFIG_PARAMETERS</a>

<a href="..\bthddi\ne-bthddi-_indication_code.md">INDICATION_CODE</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20INDICATION_PARAMETERS structure%20 RELEASE:%20(12/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>