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
ms.keywords: BRB_TYPE, BRB_ACL_ENTER_ACTIVE_MODE, bthddi/BRB_SCO_OPEN_CHANNEL_RESPONSE, BRB_SCO_GET_SYSTEM_INFO, bthddi/BRB_SCO_OPEN_CHANNEL, bthddi/BRB_SCO_TRANSFER, bthddi/BRB_GET_DEVICE_INTERFACE_STRING, bltooth.brb_type, bthddi/BRB_SCO_FLUSH_CHANNEL, BRB_L2CA_INFO_REQUEST, BRB_SCO_OPEN_UNMANAGED_CHANNEL, bthddi/BRB_L2CA_OPEN_ENHANCED_CHANNEL, BRB_GET_DEVICE_INTERFACE_STRING, bthddi/BRB_HCI_GET_LOCAL_BD_ADDR, BRB_SCO_FLUSH_CHANNEL, BRB_L2CA_OPEN_CHANNEL, bthddi/BRB_SCO_OPEN_UNMANAGED_CHANNEL, bthddi/BRB_SCO_UNREGISTER_SERVER, BRB_SCO_OPEN_CHANNEL, bthddi/BRB_SCO_OPEN_UNMANAGED_CHANNEL_RESPONSE, bthddi/BRB_L2CA_UPDATE_CHANNEL, bthddi/BRB_STORED_LINK_KEY, bth_enums_6d3541ca-7ba6-4430-9d97-55d88bea987f.xml, BRB_L2CA_UNREGISTER_SERVER, BRB_SCO_REGISTER_SERVER, bthddi/BRB_L2CA_OPEN_ENHANCED_CHANNEL_RESPONSE, BRB_REGISTER_PSM, bthddi/BRB_REGISTER_PSM, bthddi/BRB_L2CA_OPEN_CHANNEL_RESPONSE, BRB_L2CA_OPEN_CHANNEL_RESPONSE, bthddi/BRB_L2CA_ACL_TRANSFER, BRB_SCO_OPEN_UNMANAGED_CHANNEL_RESPONSE, bthddi/BRB_ACL_ENTER_ACTIVE_MODE, BRB_UNREGISTER_PSM, BRB_L2CA_PING, BRB_L2CA_REGISTER_SERVER, bthddi/BRB_TYPE, bthddi/BRB_L2CA_INFO_REQUEST, bthddi/BRB_SCO_GET_CHANNEL_INFO, BRB_L2CA_OPEN_ENHANCED_CHANNEL, BRB_SCO_OPEN_CHANNEL_RESPONSE, bthddi/BRB_UNREGISTER_PSM, BRB_SCO_GET_CHANNEL_INFO, bthddi/BRB_SCO_CLOSE_CHANNEL, BRB_SCO_CLOSE_CHANNEL, BRB_STORED_LINK_KEY, BRB_L2CA_CLOSE_CHANNEL, bthddi/BRB_SCO_REGISTER_SERVER, BRB_SCO_TRANSFER, BRB_L2CA_UPDATE_CHANNEL, bthddi/BRB_L2CA_PING, bthddi/BRB_SCO_GET_SYSTEM_INFO, BRB_TYPE enumeration [Bluetooth Devices], bthddi/BRB_L2CA_REGISTER_SERVER, BRB_HCI_GET_LOCAL_BD_ADDR, _BRB_TYPE, BRB_L2CA_ACL_TRANSFER, BRB_L2CA_OPEN_ENHANCED_CHANNEL_RESPONSE, BRB_SCO_UNREGISTER_SERVER, bthddi/BRB_L2CA_CLOSE_CHANNEL, bthddi/BRB_L2CA_UNREGISTER_SERVER, bthddi/BRB_L2CA_OPEN_CHANNEL
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	bthddi.h
apiname:
-	BRB_TYPE
product: Windows
targetos: Windows
req.typenames: BRB_TYPE
---

# _BRB_TYPE Enumeration
The <b>BRB_TYPE</b> enumeration type is used to determine the Bluetooth request block when a profile driver 
  <a href="https://msdn.microsoft.com/53a692e7-9c71-4dca-9331-32ac97b94179">builds and sends</a> a BRB.

## Syntax
````
typedef enum _BRB_TYPE { 
  BRB_HCI_GET_LOCAL_BD_ADDR                = 0x0001,
  BRB_L2CA_REGISTER_SERVER                 = 0x0100,
  BRB_L2CA_UNREGISTER_SERVER               = 0x0101,
  BRB_L2CA_OPEN_CHANNEL                    = 0x0102,
  BRB_L2CA_OPEN_CHANNEL_RESPONSE           = 0x0103,
  BRB_L2CA_CLOSE_CHANNEL                   = 0x0104,
  BRB_L2CA_ACL_TRANSFER                    = 0x0105,
  BRB_L2CA_UPDATE_CHANNEL                  = 0x0106,
  BRB_L2CA_PING                            = 0x0107,
  BRB_L2CA_INFO_REQUEST                    = 0x0108,
  BRB_REGISTER_PSM                         = 0x0109,
  BRB_UNREGISTER_PSM                       = 0x010a,
  BRB_SCO_REGISTER_SERVER                  = 0x0200,
  BRB_SCO_UNREGISTER_SERVER                = 0x0201,
  BRB_SCO_OPEN_CHANNEL                     = 0x0202,
  BRB_SCO_OPEN_CHANNEL_RESPONSE            = 0x0203,
  BRB_SCO_CLOSE_CHANNEL                    = 0x0204,
  BRB_SCO_TRANSFER                         = 0x0205,
  BRB_SCO_GET_CHANNEL_INFO                 = 0x0207,
  BRB_SCO_GET_SYSTEM_INFO                  = 0x0209,
  BRB_SCO_FLUSH_CHANNEL                    = 0x020a,
  BRB_SCO_OPEN_UNMANAGED_CHANNEL           = 0x0210,
  BRB_SCO_OPEN_UNMANAGED_CHANNEL_RESPONSE  = 0x0211,
  BRB_L2CA_OPEN_ENHANCED_CHANNEL           = 0x0212,
  BRB_L2CA_OPEN_ENHANCED_CHANNEL_RESPONSE  = 0x0213,
  BRB_ACL_ENTER_ACTIVE_MODE                = 0x0301,
  BRB_STORED_LINK_KEY                      = 0x0310,
  BRB_GET_DEVICE_INTERFACE_STRING          = 0x0320
} BRB_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>BRB_ACL_ENTER_ACTIVE_MODE</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     
     <b>BRB_ACL_ENTER_ACTIVE_MODE</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_ACL_GET_MODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>BRB_GET_DEVICE_INTERFACE_STRING</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     
     <b>BRB_GET_DEVICE_INTERFACE_STRING</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_HCI_GET_LOCAL_BD_ADDR</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     
     <b>BRB_HCI_GET_LOCAL_BD_ADDR</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_ACL_TRANSFER</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_L2CA_ACL_TRANSFER</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_CLOSE_CHANNEL</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_L2CA_CLOSE_CHANNEL</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_L2CA_INFO_REQUEST</td>
                    <td>For internal use only. Do not use.</td>
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
                    <td>BRB_L2CA_PING</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_L2CA_PING</b>.</td>
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
                    <td>BRB_L2CA_UPDATE_CHANNEL</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_L2CA_UPDATE_CHANNEL</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_REGISTER_PSM</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_REGISTER_PSM</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_CLOSE_CHANNEL</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_SCO_CLOSE_CHANNEL</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_FLUSH_CHANNEL</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_SCO_FLUSH_CHANNEL</b>.</td>
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
                    <td>BRB_SCO_REGISTER_SERVER</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_SCO_REGISTER_SERVER</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_TRANSFER</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_SCO_TRANSFER</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_SCO_UNREGISTER_SERVER</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     
     <b>BRB_SCO_UNREGISTER_SERVER</b>.</td>
                </tr>
            
                <tr>
                    <td>BRB_STORED_LINK_KEY</td>
                    <td>For internal use only. Do not use.</td>
                </tr>
            
                <tr>
                    <td>BRB_UNREGISTER_PSM</td>
                    <td>This value declares a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a> of type 
     <b>BRB_UNREGISTER_PSM</b>.</td>
                </tr>
</table>

## Remarks

The type of BRB is specified in the 
    <b>Type</b> member of the 
    <a href="..\bthddi\ns-bthddi-_brb_header.md">BRB_HEADER</a> structure. The 
    <a href="..\bthddi\nc-bthddi-pfnbth_allocate_brb.md">BthAllocateBrb</a> and 
    <a href="..\bthddi\nc-bthddi-pfnbth_initialize_brb.md">BthInitializeBrb</a> functions automatically
    set the 
    <b>Type</b> member.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Versions:\_Supported in Windows Vista, and later. Versions:\_Supported in Windows Vista, and later. |
| **Header** | bthddi.h (include Bthddi.h) |

## See Also

<a href="..\bthddi\nc-bthddi-pfnbth_allocate_brb.md">BthAllocateBrb</a>



<a href="..\bthddi\ns-bthddi-_brb.md">BRB</a>



<a href="..\bthioctl\ni-bthioctl-ioctl_internal_bth_submit_brb.md">IOCTL_INTERNAL_BTH_SUBMIT_BRB</a>



<a href="..\bthddi\nc-bthddi-pfnbth_initialize_brb.md">BthInitializeBrb</a>



<a href="..\bthioctl\ni-bthioctl-ioctl_internal_bth_submit_brb.md">IOCTL_INTERNAL_BTH_SUBMIT_BRB</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20BRB_TYPE enumeration%20 RELEASE:%20(2/15/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>