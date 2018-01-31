---
UID : NS:dispmprt._DXGK_CHILD_STATUS
title : "_DXGK_CHILD_STATUS"
author : windows-driver-content
description : The DXGK_CHILD_STATUS structure contains members that indicate the status of a child device of the display adapter.
old-location : display\dxgk_child_status.htm
old-project : display
ms.assetid : e2aba049-b51f-49b9-b0bb-c98c318dea86
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : PDXGK_CHILD_STATUS, _DXGK_CHILD_STATUS, dispmprt/DXGK_CHILD_STATUS, DXGK_CHILD_STATUS structure [Display Devices], dispmprt/PDXGK_CHILD_STATUS, display.dxgk_child_status, DmStructs_9a370d5a-9ca8-4c4f-a5cf-3361847d65e7.xml, PDXGK_CHILD_STATUS structure pointer [Display Devices], DXGK_CHILD_STATUS, *PDXGK_CHILD_STATUS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : dispmprt.h
req.include-header : Dispmprt.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
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
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXGK_CHILD_STATUS, *PDXGK_CHILD_STATUS
---

# _DXGK_CHILD_STATUS structure
The DXGK_CHILD_STATUS structure contains members that indicate the status of a child device of the display adapter.

## Syntax
````
typedef struct _DXGK_CHILD_STATUS {
  DXGK_CHILD_STATUS_TYPE Type;
  ULONG                  ChildUid;
  union {
    struct {
      BOOLEAN Connected;
    } HotPlug;
    struct {
      UCHAR Angle;
    } Rotation;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
    struct {
      BOOLEAN                         Connected;
      D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY MiracastMonitorType;
    } Miracast;
#endif 
  };
} DXGK_CHILD_STATUS, *PDXGK_CHILD_STATUS;
````

## Members


`ChildUid`

An integer, created previously by the display miniport driver, that identifies the child device for which status is being requested.

`Type`

A member of the <a href="..\dispmprt\ne-dispmprt-_dxgk_child_status_type.md">DXGK_CHILD_STATUS_TYPE</a> enumeration that indicates the type of status being requested.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dispmprt.h (include Dispmprt.h) |

## See Also

<a href="..\dispmprt\nc-dispmprt-dxgkddi_query_child_relations.md">DxgkDdiQueryChildRelations</a>

<a href="..\dispmprt\nc-dispmprt-dxgkcb_indicate_child_status.md">DxgkCbIndicateChildStatus</a>

<a href="..\dispmprt\ne-dispmprt-_dxgk_child_status_type.md">DXGK_CHILD_STATUS_TYPE</a>

<a href="..\d3dkmdt\ne-d3dkmdt-_d3dkmdt_video_output_technology.md">D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY</a>

<a href="..\dispmprt\nc-dispmprt-dxgkddi_query_child_status.md">DxgkDdiQueryChildStatus</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CHILD_STATUS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>