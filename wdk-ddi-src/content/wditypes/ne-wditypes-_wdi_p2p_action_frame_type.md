---
UID: NE:wditypes._WDI_P2P_ACTION_FRAME_TYPE
title: "_WDI_P2P_ACTION_FRAME_TYPE"
author: windows-driver-content
description: The WDI_P2P_ACTION_FRAME_TYPE enumeration defines the Wi-Fi Direct action frame types.
old-location: netvista\wdi_p2p_action_frame_type.htm
old-project: netvista
ms.assetid: 3E1C92D2-FFE0-402F-BE14-18AFB03F3FE4
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: wditypes/WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_CONFIRM, wditypes/WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_REQUEST, wditypes/WDI_P2P_ACTION_FRAME_INVITATION_RESPONSE, WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_RESPONSE, WDI_P2P_ACTION_FRAME_TYPE enumeration [Device and Driver Installation], WDI_P2P_ACTION_FRAME_INVITATION_RESPONSE, WDI_P2P_ACTION_FRAME_PROVISION_DISCOVERY_REQUEST, WDI_P2P_ACTION_FRAME_PROVISION_DISCOVERY_RESPONSE, wditypes/WDI_P2P_ACTION_FRAME_PROVISION_DISCOVERY_RESPONSE, _WDI_P2P_ACTION_FRAME_TYPE, WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_CONFIRM, WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_REQUEST, wditypes/WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_RESPONSE, WDI_P2P_ACTION_FRAME_INVITATION_REQUEST, wditypes/WDI_P2P_ACTION_FRAME_PROVISION_DISCOVERY_REQUEST, WDI_P2P_ACTION_FRAME_TYPE, netvista.wdi_p2p_action_frame_type, wditypes/WDI_P2P_ACTION_FRAME_INVITATION_REQUEST, netvista.wifi_p2p_action_frame_type, wditypes/WDI_P2P_ACTION_FRAME_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	wditypes.hpp
apiname:
-	WDI_P2P_ACTION_FRAME_TYPE
product: Windows
targetos: Windows
req.typenames: WDI_P2P_ACTION_FRAME_TYPE
req.product: Windows 10 or later.
---

# _WDI_P2P_ACTION_FRAME_TYPE Enumeration
The WDI_P2P_ACTION_FRAME_TYPE enumeration defines the Wi-Fi Direct action frame types.

## Syntax
````
typedef enum _WDI_P2P_ACTION_FRAME_TYPE { 
  WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_REQUEST        = 1,
  WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_RESPONSE       = 2,
  WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_CONFIRM        = 3,
  WDI_P2P_ACTION_FRAME_INVITATION_REQUEST            = 4,
  WDI_P2P_ACTION_FRAME_INVITATION_RESPONSE           = 5,
  WDI_P2P_ACTION_FRAME_PROVISION_DISCOVERY_REQUEST   = 6,
  WDI_P2P_ACTION_FRAME_PROVISION_DISCOVERY_RESPONSE  = 7
} WDI_P2P_ACTION_FRAME_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_CONFIRM</td>
                    <td>Wi-Fi Direct Group Owner Negotiation Confirmation.</td>
                </tr>
            
                <tr>
                    <td>WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_REQUEST</td>
                    <td>Wi-Fi Direct Group Owner Negotiation Request.</td>
                </tr>
            
                <tr>
                    <td>WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_RESPONSE</td>
                    <td>Wi-Fi Direct Group Owner Negotiation Response.</td>
                </tr>
            
                <tr>
                    <td>WDI_P2P_ACTION_FRAME_INVITATION_REQUEST</td>
                    <td>Wi-Fi Direct Invitation Request.</td>
                </tr>
            
                <tr>
                    <td>WDI_P2P_ACTION_FRAME_INVITATION_RESPONSE</td>
                    <td>Wi-Fi Direct Invitation Response.</td>
                </tr>
            
                <tr>
                    <td>WDI_P2P_ACTION_FRAME_MAX_VALUE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WDI_P2P_ACTION_FRAME_PROVISION_DISCOVERY_REQUEST</td>
                    <td>Wi-Fi Direct Provision Discovery Request.</td>
                </tr>
            
                <tr>
                    <td>WDI_P2P_ACTION_FRAME_PROVISION_DISCOVERY_RESPONSE</td>
                    <td>Wi-Fi Direct Provision Discovery Response.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | wditypes.hpp |