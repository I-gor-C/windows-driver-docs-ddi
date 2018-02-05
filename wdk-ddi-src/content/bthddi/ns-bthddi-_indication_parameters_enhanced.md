---
UID : NS:bthddi._INDICATION_PARAMETERS_ENHANCED
title : "_INDICATION_PARAMETERS_ENHANCED"
author : windows-driver-content
description : The INDICATION_PARAMETERS_ENHANCED structure is passed as the Parameters parameter to a profile driver's enhanced L2CAP Callback Function.
old-location : bltooth\indication_parameters_enhanced.htm
old-project : bltooth
ms.assetid : D0FBA555-B61F-4D6F-B93F-C77D395F2BCD
ms.author : windowsdriverdev
ms.date : 12/21/2017
ms.keywords : PINDICATION_PARAMETERS_ENHANCED structure pointer [Bluetooth Devices], *PINDICATION_PARAMETERS_ENHANCED, _INDICATION_PARAMETERS_ENHANCED, bthddi/PINDICATION_PARAMETERS_ENHANCED, bltooth.indication_parameters_enhanced, PINDICATION_PARAMETERS_ENHANCED, INDICATION_PARAMETERS_ENHANCED, bthddi/INDICATION_PARAMETERS_ENHANCED, INDICATION_PARAMETERS_ENHANCED structure [Bluetooth Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : bthddi.h
req.include-header : Bthddi.h
req.target-type : Windows
req.target-min-winverclnt : Versions:\_Supported in Windows 8 and later versions of Windows
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
req.typenames : "*PINDICATION_PARAMETERS_ENHANCED, INDICATION_PARAMETERS_ENHANCED"
---

# _INDICATION_PARAMETERS_ENHANCED structure
The INDICATION_PARAMETERS_ENHANCED structure is passed as the Parameters parameter to a profile driver's <a href="..\bthddi\nc-bthddi-pfnbthport_indication_callback_enhanced.md">enhanced L2CAP Callback Function</a>

## Syntax
````
typedef struct _INDICATION_PARAMETERS_ENHANCED {
  L2CAP_CHANNEL_HANDLE ConnectionHandle;
  BTH_ADDR             BtAddress;
  union {
    struct {
      struct {
        USHORT PSM;
      } Request;
    } Connect;
    struct {
      CHANNEL_CONFIG_PARAMETERS_ENHANCED CurrentParams;
      CHANNEL_CONFIG_PARAMETERS_ENHANCED RequestedParams;
      CHANNEL_CONFIG_PARAMETERS_ENHANCED ResponseParams;
      USHORT                             Response;
    } ConfigRequest;
    struct {
      CHANNEL_CONFIG_PARAMETERS_ENHANCED CurrentParams;
      CHANNEL_CONFIG_PARAMETERS_ENHANCED RequestedParams;
      CHANNEL_CONFIG_PARAMETERS_ENHANCED RejectedParams;
      PCO_TYPE                           UnknownTypes;
      ULONG                              NumUnknownTypes;
      CHANNEL_CONFIG_PARAMETERS_ENHANCED NewRequestParams;
      USHORT                             Response;
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
    PVOID  Reserved;
  } Parameters;
} INDICATION_PARAMETERS_ENHANCED, *PINDICATION_PARAMETERS_ENHANCED;
````

## Members


`BtAddress`

The Bluetooth address of the remote device.

`ConnectionHandle`

The L2CAP connection handle to the remote device. This handle is only valid for notifications that
     arrive over an established L2CAP connection.

`Parameters`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Versions:\_Supported in Windows 8 and later versions of Windows Versions:\_Supported in Windows 8 and later versions of Windows |
| **Header** | bthddi.h (include Bthddi.h) |