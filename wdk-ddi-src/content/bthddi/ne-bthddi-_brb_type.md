---
UID: NE:bthddi._BRB_TYPE
title: "_BRB_TYPE"
author: windows-driver-content
description: The BRB_TYPE enumeration type is used to determine the Bluetooth request block when a profile driver builds and sends a BRB.
old-location: bltooth\brb_type.htm
old-project: bltooth
ms.assetid: 590e13cf-6cbc-4a7f-a68e-ada4a5027ed2
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: BRB_ACL_ENTER_ACTIVE_MODE, BRB_GET_DEVICE_INTERFACE_STRING, BRB_HCI_GET_LOCAL_BD_ADDR, BRB_L2CA_ACL_TRANSFER, BRB_L2CA_CLOSE_CHANNEL, BRB_L2CA_INFO_REQUEST, BRB_L2CA_OPEN_CHANNEL, BRB_L2CA_OPEN_CHANNEL_RESPONSE, BRB_L2CA_OPEN_ENHANCED_CHANNEL, BRB_L2CA_OPEN_ENHANCED_CHANNEL_RESPONSE, BRB_L2CA_PING, BRB_L2CA_REGISTER_SERVER, BRB_L2CA_UNREGISTER_SERVER, BRB_L2CA_UPDATE_CHANNEL, BRB_REGISTER_PSM, BRB_SCO_CLOSE_CHANNEL, BRB_SCO_FLUSH_CHANNEL, BRB_SCO_GET_CHANNEL_INFO, BRB_SCO_GET_SYSTEM_INFO, BRB_SCO_OPEN_CHANNEL, BRB_SCO_OPEN_CHANNEL_RESPONSE, BRB_SCO_OPEN_UNMANAGED_CHANNEL, BRB_SCO_OPEN_UNMANAGED_CHANNEL_RESPONSE, BRB_SCO_REGISTER_SERVER, BRB_SCO_TRANSFER, BRB_SCO_UNREGISTER_SERVER, BRB_STORED_LINK_KEY, BRB_TYPE, BRB_TYPE enumeration [Bluetooth Devices], BRB_UNREGISTER_PSM, _BRB_TYPE, bltooth.brb_type, bth_enums_6d3541ca-7ba6-4430-9d97-55d88bea987f.xml, bthddi/BRB_ACL_ENTER_ACTIVE_MODE, bthddi/BRB_GET_DEVICE_INTERFACE_STRING, bthddi/BRB_HCI_GET_LOCAL_BD_ADDR, bthddi/BRB_L2CA_ACL_TRANSFER, bthddi/BRB_L2CA_CLOSE_CHANNEL, bthddi/BRB_L2CA_INFO_REQUEST, bthddi/BRB_L2CA_OPEN_CHANNEL, bthddi/BRB_L2CA_OPEN_CHANNEL_RESPONSE, bthddi/BRB_L2CA_OPEN_ENHANCED_CHANNEL, bthddi/BRB_L2CA_OPEN_ENHANCED_CHANNEL_RESPONSE, bthddi/BRB_L2CA_PING, bthddi/BRB_L2CA_REGISTER_SERVER, bthddi/BRB_L2CA_UNREGISTER_SERVER, bthddi/BRB_L2CA_UPDATE_CHANNEL, bthddi/BRB_REGISTER_PSM, bthddi/BRB_SCO_CLOSE_CHANNEL, bthddi/BRB_SCO_FLUSH_CHANNEL, bthddi/BRB_SCO_GET_CHANNEL_INFO, bthddi/BRB_SCO_GET_SYSTEM_INFO, bthddi/BRB_SCO_OPEN_CHANNEL, bthddi/BRB_SCO_OPEN_CHANNEL_RESPONSE, bthddi/BRB_SCO_OPEN_UNMANAGED_CHANNEL, bthddi/BRB_SCO_OPEN_UNMANAGED_CHANNEL_RESPONSE, bthddi/BRB_SCO_REGISTER_SERVER, bthddi/BRB_SCO_TRANSFER, bthddi/BRB_SCO_UNREGISTER_SERVER, bthddi/BRB_STORED_LINK_KEY, bthddi/BRB_TYPE, bthddi/BRB_UNREGISTER_PSM
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
-	BRB_TYPE
product:
- Windows
targetos: Windows
req.typenames: BRB_TYPE
---

# _BRB_TYPE Enumeration
The <b>BRB_TYPE</b> enumeration type is used to determine the Bluetooth request block when a profile driver 
  <a href="https://msdn.microsoft.com/53a692e7-9c71-4dca-9331-32ac97b94179">builds and sends</a> a BRB.

## Syntax
```
typedef enum _BRB_TYPE {
  BRB_HCI_GET_LOCAL_BD_ADDR                ,
  BRB_L2CA_REGISTER_SERVER                 ,
  BRB_L2CA_UNREGISTER_SERVER               ,
  BRB_L2CA_OPEN_CHANNEL                    ,
  BRB_L2CA_OPEN_CHANNEL_RESPONSE           ,
  BRB_L2CA_CLOSE_CHANNEL                   ,
  BRB_L2CA_ACL_TRANSFER                    ,
  BRB_L2CA_UPDATE_CHANNEL                  ,
  BRB_L2CA_PING                            ,
  BRB_L2CA_INFO_REQUEST                    ,
  BRB_REGISTER_PSM                         ,
  BRB_UNREGISTER_PSM                       ,
  BRB_SCO_REGISTER_SERVER                  ,
  BRB_SCO_UNREGISTER_SERVER                ,
  BRB_SCO_OPEN_CHANNEL                     ,
  BRB_SCO_OPEN_CHANNEL_RESPONSE            ,
  BRB_SCO_CLOSE_CHANNEL                    ,
  BRB_SCO_TRANSFER                         ,
  BRB_SCO_GET_CHANNEL_INFO                 ,
  BRB_SCO_GET_SYSTEM_INFO                  ,
  BRB_SCO_FLUSH_CHANNEL                    ,
  BRB_SCO_OPEN_UNMANAGED_CHANNEL           ,
  BRB_SCO_OPEN_UNMANAGED_CHANNEL_RESPONSE  ,
  BRB_L2CA_OPEN_ENHANCED_CHANNEL           ,
  BRB_L2CA_OPEN_ENHANCED_CHANNEL_RESPONSE  ,
  BRB_ACL_GET_MODE                         ,
  BRB_ACL_ENTER_ACTIVE_MODE                ,
  BRB_STORED_LINK_KEY                      ,
  BRB_GET_DEVICE_INTERFACE_STRING
} BRB_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>BRB_HCI_GET_LOCAL_BD_ADDR</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     
     <b>BRB_HCI_GET_LOCAL_BD_ADDR</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_REGISTER_SERVER</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_L2CA_REGISTER_SERVER</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_UNREGISTER_SERVER</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     
     <b>BRB_L2CA_UNREGISTER_SERVER</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_OPEN_CHANNEL</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_L2CA_OPEN_CHANNEL</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_OPEN_CHANNEL_RESPONSE</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     
     <b>BRB_L2CA_OPEN_CHANNEL_RESPONSE</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_CLOSE_CHANNEL</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_L2CA_CLOSE_CHANNEL</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_ACL_TRANSFER</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_L2CA_ACL_TRANSFER</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_UPDATE_CHANNEL</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_L2CA_UPDATE_CHANNEL</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_PING</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_L2CA_PING</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_INFO_REQUEST</td>
                    <td>For internal use only. Do not use.</td>
                </tr>
            
                <tr>
                    <td>BRB_REGISTER_PSM</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_REGISTER_PSM</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_UNREGISTER_PSM</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_UNREGISTER_PSM</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_REGISTER_SERVER</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_SCO_REGISTER_SERVER</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_UNREGISTER_SERVER</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     
     <b>BRB_SCO_UNREGISTER_SERVER</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_OPEN_CHANNEL</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_SCO_OPEN_CHANNEL</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_OPEN_CHANNEL_RESPONSE</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     
     <b>BRB_SCO_OPEN_CHANNEL_RESPONSE</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_CLOSE_CHANNEL</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_SCO_CLOSE_CHANNEL</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_TRANSFER</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_SCO_TRANSFER</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_GET_CHANNEL_INFO</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_SCO_GET_CHANNEL_INFO</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_GET_SYSTEM_INFO</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_SCO_GET_SYSTEM_INFO</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_FLUSH_CHANNEL</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_SCO_FLUSH_CHANNEL</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_OPEN_UNMANAGED_CHANNEL</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_SCO_OPEN_CHANNEL</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_OPEN_UNMANAGED_CHANNEL_RESPONSE</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     
     <b>BRB_SCO_OPEN_CHANNEL_RESPONSE</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_OPEN_ENHANCED_CHANNEL</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_L2CA_OPEN_CHANNEL</b>. This value is present in Windows 8 and later versions of Windows.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_OPEN_ENHANCED_CHANNEL_RESPONSE</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_L2CA_OPEN_CHANNEL_RESPONSE</b>. This value is present in Windows 8 and later versions of Windows.</td>
                </tr>
            
                <tr>
                    <td>BRB_ACL_GET_MODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>BRB_ACL_ENTER_ACTIVE_MODE</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     
     <b>BRB_ACL_ENTER_ACTIVE_MODE</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_STORED_LINK_KEY</td>
                    <td>For internal use only. Do not use.</td>
                </tr>
            
                <tr>
                    <td>BRB_GET_DEVICE_INTERFACE_STRING</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     
     <b>BRB_GET_DEVICE_INTERFACE_STRING</b>.</td>
                </tr>
</table>

## Remarks

The type of BRB is specified in the 
    <b>Type</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff536612">BRB_HEADER</a> structure. The 
    <a href="https://msdn.microsoft.com/e1ac9d4c-75e2-4d37-86d7-3c3f1486222e">BthAllocateBrb</a> and 
    <a href="https://msdn.microsoft.com/0b822d28-edaa-40cc-a678-112a356d9022">BthInitializeBrb</a> functions automatically
    set the 
    <b>Type</b> member.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Versions:\_Supported in Windows Vista, and later. Versions:\_Supported in Windows Vista, and later. |
| **Header** | bthddi.h (include Bthddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536612">BRB_HEADER</a>



<a href="https://msdn.microsoft.com/e1ac9d4c-75e2-4d37-86d7-3c3f1486222e">BthAllocateBrb</a>



<a href="https://msdn.microsoft.com/0b822d28-edaa-40cc-a678-112a356d9022">BthInitializeBrb</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536751">IOCTL_INTERNAL_BTH_SUBMIT_BRB</a>