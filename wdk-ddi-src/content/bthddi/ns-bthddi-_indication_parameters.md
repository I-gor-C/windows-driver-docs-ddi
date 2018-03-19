---
UID: NS:bthddi._INDICATION_PARAMETERS
title: "_INDICATION_PARAMETERS"
author: windows-driver-content
description: The INDICATION_PARAMETERS structure is passed as the Parameters parameter to a profile driver's L2CAP Callback Function.
old-location: bltooth\indication_parameters.htm
old-project: bltooth
ms.assetid: fc93ab8a-01d2-4827-8d89-06f09bf10456
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PINDICATION_PARAMETERS, INDICATION_PARAMETERS, INDICATION_PARAMETERS structure [Bluetooth Devices], PINDICATION_PARAMETERS, PINDICATION_PARAMETERS structure pointer [Bluetooth Devices], _INDICATION_PARAMETERS, bltooth.indication_parameters, bth_structs_8cf076cf-a280-49ee-bbe6-cc54e854905e.xml, bthddi/INDICATION_PARAMETERS, bthddi/PINDICATION_PARAMETERS"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
-	INDICATION_PARAMETERS
product: Windows
targetos: Windows
req.typenames: "*PINDICATION_PARAMETERS, INDICATION_PARAMETERS, *PINDICATION_PARAMETERS"
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


`ConnectionHandle`

The L2CAP connection handle to the remote device. This handle is only valid for notifications that
     arrive over an established L2CAP connection.

`BtAddress`

The Bluetooth address of the remote device.

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
| **Windows version** | Versions:\_Supported in Windows Vista, and later. Versions:\_Supported in Windows Vista, and later. |
| **Header** | bthddi.h (include Bthddi.h) |

## See Also

<a href="..\bthddi\ne-bthddi-_indication_code.md">INDICATION_CODE</a>



<a href="..\bthddi\ne-bthddi-_l2cap_disconnect_reason.md">L2CAP_DISCONNECT_REASON</a>



<a href="..\bthddi\ns-bthddi-_l2cap_config_option.md">L2CAP_CONFIG_OPTION</a>



<a href="..\bthddi\nc-bthddi-pfnbthport_indication_callback.md">L2CAP Callback Function</a>



<a href="..\bthddi\ns-bthddi-_channel_config_parameters.md">CHANNEL_CONFIG_PARAMETERS</a>