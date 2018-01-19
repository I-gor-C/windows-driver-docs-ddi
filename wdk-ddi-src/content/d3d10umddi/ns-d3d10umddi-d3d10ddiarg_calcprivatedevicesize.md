---
UID : NS:d3d10umddi.D3D10DDIARG_CALCPRIVATEDEVICESIZE
title : D3D10DDIARG_CALCPRIVATEDEVICESIZE
author : windows-driver-content
description : The D3D10DDIARG_CALCPRIVATEDEVICESIZE structure describes the parameters that the user-mode display driver uses to calculate the size of a memory block that the driver requires to store frequently-accessed data.
old-location : display\d3d10ddiarg_calcprivatedevicesize.htm
old-project : display
ms.assetid : 79bb55db-dd4d-4cad-927e-e1126463bded
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D10DDIARG_CALCPRIVATEDEVICESIZE, D3D10DDIARG_CALCPRIVATEDEVICESIZE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3D10DDIARG_CALCPRIVATEDEVICESIZE
req.alt-loc : d3d10umddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : D3D10DDIARG_CALCPRIVATEDEVICESIZE
---

# D3D10DDIARG_CALCPRIVATEDEVICESIZE structure
The D3D10DDIARG_CALCPRIVATEDEVICESIZE structure describes the parameters that the user-mode display driver uses to calculate the size of a memory block that the driver requires to store frequently-accessed data.

## Syntax
````
typedef struct D3D10DDIARG_CALCPRIVATEDEVICESIZE {
  UINT Interface;
  UINT Version;
  UINT Flags;
} D3D10DDIARG_CALCPRIVATEDEVICESIZE;
````

## Members

        
            `Flags`

            [in] A valid bitwise OR of flag values that identify how to create a rendering device. The Direct3D runtime supports the following flags:
        
            `Interface`

            [in] The Microsoft Direct3D interface version. The high 16 bits store the major release number (such as 10, 11, and so on); the low 16 bits store the minor release number (such as 0, 1, 2, and so on). The minor release number will be increased when a change to the interface is released.
        
            `Version`

            [in] A number that the driver can use to identify when the Direct3D runtime was built. The high 16 bits represent the build number; the low 16 bits represent the revision number. 

The driver is required only to monitor the high 16 bits. The driver should ensure that the runtime build version that is passed in is greater than or equal to the current build version of the driver. The driver should return a failure from its <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_calcprivatedevicesize.md">CalcPrivateDeviceSize</a> function if the passed in build version is incompatible.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

    ## See Also

        <dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_calcprivatedevicesize.md">CalcPrivateDeviceSize</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10DDIARG_CALCPRIVATEDEVICESIZE structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>