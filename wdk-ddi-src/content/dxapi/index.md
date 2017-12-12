---
UID: NA:
---

# Dxapi.h header

## -description

This header is used by Display. For more information, see
- [Display](../_display/index.md)

Dxapi.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [DxApi function](nf-dxapi-dxapi.md) | The DxApi function accepts commands from the hardware decoder's video capture driver to access the DxApi interface functions that are implemented in a video miniport driver. |
| [DxApiGetVersion function](nf-dxapi-dxapigetversion.md) | Do not use the DxApiGetVersion function; use the DxApi function along with the DD_DXAPI_GETVERSIONNUMBER function identifier instead.The DxApiGetVersion function returns a Direct Sound version number of 4.02. |
