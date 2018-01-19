---
UID : NS:d3dumddi._DXVAHDDDI_VPDEVCAPS
title : _DXVAHDDDI_VPDEVCAPS
author : windows-driver-content
description : The DXVAHDDDI_VPDEVCAPS structure describes the video processor capabilities that the decode device supports.
old-location : display\dxvahdddi_vpdevcaps.htm
old-project : display
ms.assetid : 25b15c20-e23a-438f-a02e-aedc26498828
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXVAHDDDI_VPDEVCAPS, DXVAHDDDI_VPDEVCAPS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Windows
req.target-min-winverclnt : DXVAHDDDI_VPDEVCAPS is supported starting with Windows 7.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXVAHDDDI_VPDEVCAPS
req.alt-loc : d3dumddi.h
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
req.typenames : DXVAHDDDI_VPDEVCAPS
---

# _DXVAHDDDI_VPDEVCAPS structure
The DXVAHDDDI_VPDEVCAPS structure describes the video processor capabilities that the decode device supports.

## Syntax
````
typedef struct _DXVAHDDDI_VPDEVCAPS {
  UINT        Reserved;
  UINT        DeviceCaps;
  UINT        FeatureCaps;
  UINT        FilterCaps;
  UINT        InputFormatCaps;
  D3DDDI_POOL InputPool;
  UINT        OutputFormatCount;
  UINT        InputFormatCount;
  UINT        VideoProcessorCount;
  UINT        MaxInputStreams;
  UINT        MaxStreamStates;
} DXVAHDDDI_VPDEVCAPS;
````

## Members

        
            `DeviceCaps`

            [out] A bitwise OR of the following values from the DXVAHDDDI_DEVICE_CAPS enumeration to indicate device-specific capabilities.
        
            `FeatureCaps`

            [out] A bitwise OR of the following values from the DXVAHDDDI_FEATURE_CAPS enumeration to indicate feature-specific capabilities.
        
            `FilterCaps`

            [out] A bitwise OR of the following values from the DXVAHDDDI_FILTER_CAPS enumeration to indicate filter-specific capabilities.
        
            `InputFormatCaps`

            [out] A bitwise OR of the following values from the DXVAHDDDI_INPUT_FORMAT_CAPS enumeration to indicate input-format-specific capabilities.
        
            `InputFormatCount`

            [out] The number of supported input formats. The driver returns an array of <a href="..\d3dukmdt\ne-d3dukmdt-_d3dddiformat.md">D3DDDIFORMAT</a> enumeration types for the input formats that the decode device supports when the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a> function is called with the D3DDDICAPS_DXVAHD_GETVPINPUTFORMATS value set.
        
            `InputPool`

            [out] A <a href="..\d3dukmdt\ne-d3dukmdt-_d3dddi_pool.md">D3DDDI_POOL</a>-typed value that indicates the memory pool from which the input surfaces should be allocated.
        
            `MaxInputStreams`

            [out] The driver can enable the maximum number of input streams at a time.
        
            `MaxStreamStates`

            [out] The maximum number of stream states.
        
            `OutputFormatCount`

            [out] The number of supported output formats. The driver returns an array of <a href="..\d3dukmdt\ne-d3dukmdt-_d3dddiformat.md">D3DDDIFORMAT</a> enumeration types for the output formats that the decode device supports when the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a> function is called with the D3DDDICAPS_DXVAHD_GETVPOUTPUTFORMATS value set.
        
            `Reserved`

            [in] Reserved. Must be zero.
        
            `VideoProcessorCount`

            [out] The number of supported video processors. The driver returns an array of <a href="..\d3dumddi\ns-d3dumddi-_dxvahdddi_vpcaps.md">DXVAHDDDI_VPCAPS</a> structures for the capabilities for each video processor that the decode device supports when the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a> function is called with the D3DDDICAPS_DXVAHD_GETVPCAPS value set.

    ## Remarks
        The user-mode display driver returns a pointer to a populated DXVAHDDDI_VPDEVCAPS structure in the <b>pData</b> member of the <a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_getcaps.md">D3DDDIARG_GETCAPS</a> structure when its <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a> function is called with the D3DDDICAPS_DXVAHD_GETVPDEVCAPS value set in the <b>Type</b> member of D3DDDIARG_GETCAPS.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |

    ## See Also

        <dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_getcaps.md">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt-_d3dddiformat.md">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt-_d3dddi_pool.md">D3DDDI_POOL</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-_dxvahdddi_vpcaps.md">DXVAHDDDI_VPCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_VPDEVCAPS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>